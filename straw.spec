
#
# todo:
# - pl description
# - make s/python2.2/python/g patch
# - recompile straw python modules, so there will be *.pyo files installed
#   and paths will be correct when exception is thrown
#

%include /usr/lib/rpm/macros.python

Summary:	News aggregator
Summary(pl):	Czytnik wiadomo¶ci
Name:		straw
Version:	0.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.nongnu.org/straw
BuildRequires:	libgnomeui-devel >= 2.0.5
Requires:	python-gnome-ui
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6
%define _mandir %{_prefix}/man

%description
News aggregators read news, weblog or other feeds over the web and
aggregate them so the news items are readable from a single place,
regardless of their source. The data format aggregators utilize to do their
job is called RSS, standing either for Really Simple Syndication or RDF
Site Summary, depending on who you ask. At the moment, there are two
different, incompatible specifications, with different objectives: RSS
0.9x/RSS 2.0 and RSS 1.0. Straw supports both of them.

To find feeds to subscribe to, look for a white on orange XML icon, XML
icon, on web sites.  You could also use a centralized syndication service,
such as Syndic8.com.

%prep
%setup -q

%build
%{__make} PYTHON=python

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/applications,%{_pixmapsdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	PYTHON=python \
	LIBDIR=$RPM_BUILD_ROOT%{py_sitedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{py_sitedir}/%{name}
%{_datadir}/applications/*
%{_pixmapsdir}/*
