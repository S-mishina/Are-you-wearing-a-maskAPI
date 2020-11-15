import asyncio
import csv
import time
import datetime
from playsound import playsound
async def handle_echo(reader, writer):
    day = datetime.date.today()
    time1 = datetime.datetime.now()
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    print(message)
    meg=str(message)
    writer.write(data)
    await writer.drain()
    if meg=="1":
        playsound('ok.wav')
        print("OK")
        with open("mask.csv","a")as csv_file:
            writer1 = csv.writer(csv_file)
            writer1.writerow([str(day),  str(time1.hour)+":"+str(time1.minute)+":"+str(time1.second), 'OK'])
            print(str(day))
            print(str(time1.hour)+":"+str(time1.minute)+":"+str(time1.second))
            print("CSVファイルを書き込みました.")

    if meg=="2":
        playsound('nomask.wav')
        print("NG")
        with open("mask.csv","a")as csv_file:
            writer1 = csv.writer(csv_file)
            writer1.writerow([str(day), str(time1.hour)+":"+str(time1.minute)+":"+str(time1.second), 'NG'])
            print(str(day))
            print(str(time1.hour)+":"+str(time1.minute)+":"+str(time1.second))
            print("CSVファイルを書き込みました.")



    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())