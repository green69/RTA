# Name: Downloading Files With Bitsadmin
# Author: Christopher Mulligan https://www.linkedin.com/in/christopher-mulligan-ceh-773995a3/
# RTA: bitsadmin_webrequest.py
# ATT&CK: S0190
# Description: Uses bitadmin to download a file.

import common

#MY_DLL = common.get_path("bin", "mydll.dll")


#@common.dependencies(MY_DLL)
def main():
    # http server will terminate on main thread exit
    # if daemon is True
    server, ip, port = common.serve_web()

    #uri = "bin/mydll.dll"
    target_file = "JustDoIt180723.txt"
    common.clear_web_cache()
    #url = "http://{ip}:{port}/{uri}".format(ip=ip, port=port, uri=uri)
    url = "https://s3.us-east-2.amazonaws.com/untest.xv8r9hdd4zq5.ca/JustDoIt180723.txt"
    common.execute(["bitsadmin", "/transfer", "myDownloadJob", "/download", "/priority", "normal", url, "c:\\"+target_file])

    server.shutdown()
    common.remove_file(target_file)


if __name__ == "__main__":
    exit(main())
