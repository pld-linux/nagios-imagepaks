# TODO
# - drop the icons other than base, they are quite useless and find better and
#   complete (perhaps some desktop?) icons?
Summary:	Nagios Image Packs
Summary(pl.UTF-8):	Zestawy obrazków dla Nagiosa
Name:		nagios-imagepaks
Version:	1.0
Release:	4
License:	Open Source
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/nagios/imagepak-base.tar.gz
# Source0-md5:	35b75ece533dfdf4963a67ce4e77fc4a
Source1:	http://dl.sourceforge.net/nagios/imagepak-bernhard.tar.gz
# Source1-md5:	cd711110929fd2487234172a533e82c5
Source2:	http://dl.sourceforge.net/nagios/imagepak-cook.tar.gz
# Source2-md5:	248d682712c594fc4734c0158d2d2ee4
Source3:	http://dl.sourceforge.net/nagios/imagepak-didier.tar.gz
# Source3-md5:	83e98389e5b7fb39d2c0e3a96d5ca585
Source4:	http://dl.sourceforge.net/nagios/imagepak-remus.tar.gz
# Source4-md5:	76595744dae8153c921c4af6bf18383d
Source5:	http://dl.sourceforge.net/nagios/imagepak-satrapa.tar.gz
# Source5-md5:	3ed26d8b49379e0dc14f448d5c2a70c3
Source6:	http://dl.sourceforge.net/nagios/imagepak-werschler.tar.gz
# Source6-md5:	1a9cba019ccd27756977821aa735c40f
Source7:	http://glen.alkohol.ee/pld/nagios/imagepak-pld-20090804.tar.bz2
# Source7-md5:	e6ea8e9fa534ae8edea462c6ee5fa3ed
# Source7License: Public Domain - http://glen.alkohol.ee/pld/nagios/
Source8:	http://www.monitoringexchange.org/attachment/download/Artwork/Image-Packs/Network-Symbols/symbols-v1.1.tar.gz
# Source8-md5:	2c40462f698838c3c528fe1aea42e308
# Source8Download:	http://www.nagiosexchange.org/cgi-bin/jump.cgi?ID=1412&view=File2;d=1
# Source8License: GPL v2
# Source8URL:	http://www.monitoringexchange.org/inventory/Artwork/Image-Packs/Network-Symbols
Source9:	mandriva.png
# Source9-md5:	72e3a8d8c4bcc05dafe53151253997a4
URL:		http://www.nagiosexchange.org/cgi-bin/pages/Artwork/Image_Packs/index.html
BuildRequires:	ImageMagick
BuildRequires:	gd-progs
BuildRequires:	tar >= 1:1.15.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_logodir	/usr/share/nagios/images/logos

%description
Image packs are provided so that you have some colorful OS and device
images to beautify your CGIs in Nagios. Each pack includes GIF, JPEG,
PNG, and GD2 versions of each icon.

%description -l pl.UTF-8
Ten pakiet dostarcza zestawy obrazków, dzięki którym można,
przypisując kolorowe symbole do systemów operacyjnych i urządzeń,
uatrakcyjnić skrypty CGI Nagiosa. Każdy zestaw zawiera wersje GIF,
JPEG, PNG i GD2 każdej ikony.

%prep
%setup -qcT
install -d logos/{bernhard,cook}
tar -xz -C logos -f %{SOURCE0}
tar -xz -C logos/bernhard --strip-components=1 -f %{SOURCE1}
tar -xz -C logos/cook -f %{SOURCE2}
# .tar.gz junk
rm -f logos/cook/README
tar -xz -C logos -f %{SOURCE3}
tar -xz -C logos -f %{SOURCE4}
tar -xz -C logos -f %{SOURCE5}
tar -xz -C logos -f %{SOURCE6}
tar -xj -C logos/base --strip-components=1 -f %{SOURCE7}
tar -xz -C logos -f %{SOURCE8}
rm -f logos/symbols/LICENSE # GPL v2
cp %{SOURCE9} logos/base

%build
# shiny mandriva icon
convert logos/base/mandriva.png logos/base/mandriva.gif
convert logos/base/mandriva.png logos/base/mandriva.jpg
pngtogd2 logos/base/mandriva.png logos/base/mandriva.gd2 0 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_logodir}
cp -a logos/* $RPM_BUILD_ROOT%{_logodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_logodir}/*
