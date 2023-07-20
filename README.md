# Discord Image Replacer
A simple HTTP server that returns an image of choice upon any GET request to `cdn.discordapp.com`. Just for fun, and potentially some trolling.

Made using Python's standard `http.server`, `ssl` and `mimetypes` module.

## Running
### Dependencies
You will need Python 3.7+ installed on your system. You can download it [here](https://www.python.org/downloads/) if you are on Windows, or by using a package manager in your Linux distribution.

You also need [`mkcert`](https://github.com/FiloSottile/mkcert#installation), follow the instructions on the GitHub page to install it.

### Steps
1. Clone the repository, either by using `git clone` or by downloading the ZIP file.
2. Generate an SSL certificate for the server.
    - First, install the local CA certificate by running `mkcert -install`.
    - Then, generate a certificate for the server by running `mkcert cdn.discordapp.com -cert-file cert.pem -key-file key.pem`.
3. Add an entry to your hosts file to redirect `cdn.discordapp.com` to `127.0.0.1`.
    - On Windows, you can find the hosts file at `C:\Windows\System32\drivers\etc\hosts`.
    - On Linux, you can find the hosts file at `/etc/hosts`.
    - Add the following line to the end of the file:
      ```
      127.0.0.1	cdn.discordapp.com
      ```
4. Run the server by running `python3 main.py /path/to/image.png` in the directory you cloned the repository to, replacing `/path/to/image.png` with the path to the image you want to use.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.