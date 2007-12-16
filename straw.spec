Summary:	News aggregator
Summary(pl.UTF-8):	Narzędzie zbierające wiadomości
Name:		straw
Version:	0.27
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/straw/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	d21249c82b14570fe2c61e114d1d2ea7
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/straw/
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2 >= 2.4.0
Requires:	python-adns
Requires:	python-gnome-extras-egg
Requires:	python-gnome-extras-gtkhtml
Requires:	python-gnome-gconf
Requires:	python-gnome-ui
Requires:	python-gnome-vfs
%pyrequires_eq	python-modules
Requires:	python-pygtk-glade >= 2:2.8.0
Requires:	python-pyorbit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News aggregators read news, weblog or other feeds over the web and
aggregate them so the news items are readable from a single place,
regardless of their source. The data format aggregators utilize to do
their job is called RSS, standing either for Really Simple Syndication
or RDF Site Summary, depending on who you ask. At the moment, there
are two different, incompatible specifications, with different
objectives: RSS 0.9x/RSS 2.0 and RSS 1.0. Straw supports both of them.

To find feeds to subscribe to, look for a white on orange XML icon,
XML icon, on web sites. You could also use a centralized syndication
service, such as Syndic8.com.

%description -l pl.UTF-8
Narzędzia zbierające czytają wiadomości, logi sieciowe lub inne źródła
z sieci i zbierają je, dzięki czemu wszystkie wiadomości są dostępne
do czytania w jednym miejscu, niezależnie od źródła. Narzędzia te
używają formatu danych o nazwie RSS (Really Simple Syndication lub RDF
Site Summary - jak kto woli). Aktualnie są dwie różne, niekompatybilne
specyfikacje, o różnych celach: RSS 0.9x/RSS 2.0 oraz RSS 1.0. Straw
obsługuje oba.

Aby znaleźć źródła do których można się zapisać, należy szukać
biało-pomarańczowych ikonek XML na stronach WWW. Można także
skorzystać z centralnego serwisu takiego jak Syndic8.com.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--install-purelib=%{py_sitedir} \
	--optimize=2 \
	--disable-modules-check \
	--disable-schemas-install

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*.py
install -D data/straw.schemas $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/straw.schemas

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install straw.schemas

%preun
%gconf_schema_uninstall straw.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{py_sitedir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
