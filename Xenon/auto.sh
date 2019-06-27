chmod 777 *
cd dlr
chmod 777 *
sh build.sh
cp /root/dlr/release/* /root/loader/bins
sh /root/build.sh
mkdir /var/www/html/bins
cp /root/release/* /var/www/html/bins

