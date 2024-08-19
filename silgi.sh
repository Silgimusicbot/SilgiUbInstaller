Userator+="\n? ????? ??????? ?? - AVTOMATIK QURULUM �?"
MESAJ+="\n "
MESAJ+="\n✅Yeniliklər kanalımız: @silgiubplugin"
MESAJ+="\n✅Dəstək qrupumuz: @silgiuserbot"
MESAJ+="\n "
KOMEK+="\n "
BOSLUQ="\n "
clear
echo -e $BOSLUQ
echo -e $BOSLUQ
pkg update -y
clear
echo -e $BOSLUQ
apt upgrade -y
echo -e $BOSLUQ
echo -e $MESAJ
echo -e $BOSLUQ
echo "Python yüklənir..."
echo -e $BOSLUK
pkg install python -y
pip install --upgrade pip
clear
echo -e $MESAJ
echo -e $BOSLUQ
echo "Git yüklənir..."
echo -e $BOSLUQ
pkg install git -y
clear
echo -e $MESAJ
echo -e $BOSLUQ
echo "Telethon yüklənir..."
echo -e $BOSLUQ
pip install telethon
clear
echo -e $MESAJ
echo -e $BOSLUQ
echo "Faylları yükləyirəm..."
echo -e $BOSLUQ
rm -rf SilgiUb?nstaller
git clone https://github.com/Silgimusicbot/SilgiUserbot
clear
echo -e $BOSLUK
echo -e $MESAJ
echo -e $BOSLUQ
echo -e $BOSLUQ
cd SilgiUb?nstaller
pip install -r requirements.txt
python -m silgi_installer
