Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przegl±darka obrazków
Summary(pt_BR):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	2.8.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	2bad4006f3ccf15b0153d7b9facbc961
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.8.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	eel-devel >= 2.8.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.8.2
BuildRequires:	intltool
Buildrequires:	libart_lgpl-devel >= 2.3.16
Buildrequires:	libexif-devel >= 1:0.5.12
Buildrequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeprint-devel >= 2.8.0
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libgnomeprintui-devel >= 2.8.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.8.1
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	xft-devel >= 2.1.2
Requires(post):	GConf2
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl
Eye of GNOME (Oko GNOME) jest narzêdziem do ogl±dania/katalogowania
obrazków.

%description -l pt_BR
Aplicativo para visualizar imagens chamado Eye of GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoheader}
gnome-doc-common
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%post
umask 022
%gconf_schema_install
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
