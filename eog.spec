Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przegl±darka obrazków
Name:		eog
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/eog/%{name}-%{version}.tar.gz
Source1:	%{name}.gif
Patch0:		%{name}-am_ac.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel
BuildRequires:	bonobo-devel >= 0.35
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.25
BuildRequires:	intltool
BuildRequires:	libglade-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	oaf-devel >= 0.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl
Eye of GNOME (Oko GNOME) jest narzêdziem do ogl±dania/katalogowania
obrazków.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
libtoolize --copy --force
xml-i18n-toolize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
%configure \
	--with-bonobo
%{__make}
		
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/*
%{_datadir/idl/*.idl
%{_datadir}/%{name}
%{_datadir}/gnome/ui
%{_datadir}/oaf/*.oaf
%{_pixmapsdir}/%{name}
