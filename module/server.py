import asyncio
import sys
import os

class ServerMinecraft:
    def __init__(self, name, server_directory, jar_name="server.jar"):
        self.name = name
        self.server_directory = server_directory  # Folder tempat server.jar berada
        self.jar_name = jar_name                  # Nama file jar-nya
        self.process = None                       # Tempat menyimpan proses server yang aktif
        self.reader_task = None                   # Tempat menyimpan tugas pembaca log async

    async def start(self):
        """Menyalakan server Minecraft"""
        if self.process:
            print(f"[{self.name}] Server sudah dalam kondisi berjalan!")
            return

        print(f"[{self.name}] Sedang menyalakan server...")
        
        # Pindah ke directory server agar file eula.txt, server.properties dll terbaca dengan benar
        os.chdir(self.server_directory)

        # Jalankan server menggunakan asyncio subprocess
        self.process = await asyncio.create_subprocess_exec(
            'java', '-Xmx1024M', '-Xms1024M', '-jar', self.jar_name, 'nogui',
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT
        )

        # Mulai membaca output secara background (non-blocking)
        self.reader_task = asyncio.create_task(self._read_output())
        print(f"[{self.name}] Proses berhasil dijalankan.")

    async def _read_output(self):
        """Fungsi internal untuk membaca log server secara real-time"""
        try:
            while self.process and self.process.stdout:
                line = await self.process.stdout.readline()
                if not line:
                    break
                # Menampilkan log ke terminal Python
                print(f"[{self.name}-LOG]: {line.decode('utf-8', errors='ignore').strip()}")
        except asyncio.CancelledError:
            # Mengantisipasi jika task pembaca dihentikan paksa saat server stop
            pass

    async def send_command(self, command: str):
        """Mengirimkan perintah ke dalam console Minecraft"""
        if not self.process or not self.process.stdin:
            print(f"[{self.name}] Gagal: Server sedang tidak berjalan.")
            return

        # Kirim perintah dalam bentuk bytes, wajib diakhiri dengan \n (Enter)
        full_command = f"{command}\n"
        self.process.stdin.write(full_command.encode())
        await self.process.stdin.drain()
        print(f"[{self.name}-COMMAND SENT]: {command}")

    async def stop(self):
        """Mematikan server secara aman"""
        if not self.process:
            print(f"[{self.name}] Server memang sudah mati.")
            return

        print(f"[{self.name}] Mengirim perintah stop...")
        await self.send_command("stop")

        # Tunggu proses Java benar-benar selesai selesai
        await self.process.wait()
        
        # Batalkan task pembaca log agar bersih dari memory
        if self.reader_task:
            self.reader_task.cancel()

        # Reset status proses menjadi None kembali
        self.process = None
        self.reader_task = None
        print(f"[{self.name}] Server telah mati total.")

# --- CARA MENJALANKANNYA ---
async def main():
    # Ganti path ini sesuai folder server Minecraft-mu di komputer
    PATH_SERVER_1 = r"C:\Users\NamaKamu\Desktop\MinecraftServer"

    # 1. Inisialisasi object server dari Class
    server_lobby = ServerMinecraft(name="LobbyServer", server_directory=PATH_SERVER_1)

    # 2. Nyalakan server
    await server_lobby.start()

    # Tunggu 25 detik (simulasi membiarkan server booting)
    await asyncio.sleep(25)

    # 3. Kirim perintah tes
    await server_lobby.send_command("say Halo dari Python Class!")
    await server_lobby.send_command("whitelist add sebuah_nama")

    # Tunggu 10 detik lagi
    await asyncio.sleep(10)

    # 4. Matikan server
    await server_lobby.stop()

if __name__ == "__main__":
    # Fix khusus Windows agar tidak error saat menjalankan async subprocess
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        
    asyncio.run(main())

mypath = "./content/savedServers/bedrock-server-1.26.20.5/bedrock_server"