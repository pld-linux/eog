Summary:	The Eye of GNOME image viewer
Name:		eog
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org//pub/GNOME/unstable/sources/eog/%{name}-%{version}.tar.gz
Source1:	%{name}.gif
URL:		http://www.gnome.org/
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Eye of GNOME is a tool for viewing/cataloging images.

%prep
%setup -q

%build
gettextize --copy --force
%configure \
	--with-bonobo
%{__make}
		
%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/*
%{_pixmapsdir}/*
%{_datadir}/icons/*
