%include	/usr/lib/rpm/macros.python
Summary:	News aggregator
Summary(pl):	Narzêdzie zbieraj±ce wiadomo¶ci
Name:		straw
Version:	0.22
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	8cdd2ad3c6d8f4e120eae003831152a0
URL:		http://www.nongnu.org/straw/
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
Requires(post):	GConf2 >= 2.4.0
Requires:	python-adns
Requires:	python-gnome-gconf
Requires:	python-gnome-gtkhtml
Requires:	python-gnome-ui
Requires:	python-gnome-vfs
Requires:	python-modules >= 2.3
Requires:	python-mx-DateTime
Requires:	python-pygtk-glade
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

%description -l pl
Narzêdzia zbieraj±ce czytaj± wiadomo¶ci, logi sieciowe lub inne ¼ród³a
z sieci i zbieraj± je, dziêki czemu wszystkie wiadomo¶ci s± dostêpne
do czytania w jednym miejscu, niezale¿nie od ¼ród³a. Narzêdzia te
u¿ywaj± formatu danych o nazwie RSS (Really Simple Syndication lub RDF
Site Summary - jak kto woli). Aktualnie s± dwie ró¿ne, niekompatybilne
specyfikacje, o ró¿nych celach: RSS 0.9x/RSS 2.0 oraz RSS 1.0. Straw
obs³uguje oba.

Aby znale¼æ ¼ród³a do których mo¿na siê zapisaæ, nale¿y szukaæ
bia³o-pomarañczowych ikonek XML na stronach WWW. Mo¿na tak¿e
skorzystaæ z centralnego serwisu takiego jak Syndic8.com.

%prep
%setup -q

mv po/{no,nb}.po

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{py_sitedir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
