%include	/usr/lib/rpm/macros.python
Summary:	News aggregator
Summary(pl):	Narz�dzie zbieraj�ce wiadomo�ci
Name:		straw
Version:	0.19
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}.pkg/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	93af66a84e97034d4981c0452995ccf7
Patch0:		%{name}-python.patch
Patch1:		%{name}-sax_handler.patch
URL:		http://www.nongnu.org/straw/
BuildRequires:	libgnomeui-devel >= 2.0.5
Requires:	python-adns
Requires:	python-gnome-gtkhtml
Requires:	python-gnome-ui
Requires:	python-gnome-vfs
Requires:	python-modules >= 2.3
Requires:	python-mx-DateTime
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
Narz�dzia zbieraj�ce czytaj� wiadomo�ci, logi sieciowe lub inne �r�d�a
z sieci i zbieraj� je, dzi�ki czemu wszystkie wiadomo�ci s� dost�pne
do czytania w jednym miejscu, niezale�nie od �r�d�a. Narz�dzia te
u�ywaj� formatu danych o nazwie RSS (Really Simple Syndication lub RDF
Site Summary - jak kto woli). Aktualnie s� dwie r�ne, niekompatybilne
specyfikacje, o r�nych celach: RSS 0.9x/RSS 2.0 oraz RSS 1.0. Straw
obs�uguje oba.

Aby znale�� �r�d�a do kt�rych mo�na si� zapisa�, nale�y szuka�
bia�o-pomara�czowych ikonek XML na stronach WWW. Mo�na tak�e
skorzysta� z centralnego serwisu takiego jak Syndic8.com.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	PYTHON=python

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	PYTHON=python \
	LIBDIR=$RPM_BUILD_ROOT%{py_sitedir}/%{name}

install src/lib/*.py $RPM_BUILD_ROOT%{py_sitedir}/%{name}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/%{name}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
