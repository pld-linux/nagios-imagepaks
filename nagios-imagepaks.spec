Summary:	Nagios Image Packs
Summary(pl):	Zestawy obrazków dla Nagiosa
Name:		nagios-imagepaks
Version:	1.0
Release:	1
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
Source7:	http://glen.alkohol.ee/pld/nagios/imagepak-pld-20050402.4.tar.bz2
# Source7-md5:	9a635a4e2fed2460d2851cb35c658aba
URL:		http://www.nagiosexchange.org/Image_Packs.75.0.html
BuildRequires:	tar >= 1:1.15.1
Requires:	nagios-cgi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_logodir	/usr/share/nagios/images/logos

%description
Image packs are provided so that you have some colorful OS and device
images to beautify your CGIs in Nagios. Each pack includes GIF, JPEG,
PNG, and GD2 versions of each icon.

%description -l pl
Ten pakiet dostarcza zestawy obrazków, dziêki którym mo¿na,
przypisuj±c kolorowe symbole do systemów operacyjnych i urz±dzeñ,
uatrakcyjniæ skrypty CGI Nagiosa. Ka¿dy zestaw zawiera wersje GIF, JPEG,
PNG i GD2 ka¿dej ikony.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_logodir}/{bernhard,cook}
tar -xz -C $RPM_BUILD_ROOT%{_logodir} -f %{SOURCE0}
tar -xz -C $RPM_BUILD_ROOT%{_logodir}/bernhard --strip-components=1 -f %{SOURCE1}
tar -xz -C $RPM_BUILD_ROOT%{_logodir}/cook -f %{SOURCE2}
tar -xz -C $RPM_BUILD_ROOT%{_logodir} -f %{SOURCE3}
tar -xz -C $RPM_BUILD_ROOT%{_logodir} -f %{SOURCE4}
tar -xz -C $RPM_BUILD_ROOT%{_logodir} -f %{SOURCE5}
tar -xz -C $RPM_BUILD_ROOT%{_logodir} -f %{SOURCE6}
tar -xj -C $RPM_BUILD_ROOT%{_logodir}/base --strip-components=1 -f %{SOURCE7}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_logodir}/*
