Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przegl±darka obrazków
Summary(pt_BR):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	2.5.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	35c2ea0c1225322b4880cffb329982f7
Patch0:		%{name}-libtool.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.5.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	eel-devel >= 2.5.3
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.5.3
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.5.1
BuildRequires:	libbonoboui-devel >= 2.5.1
BuildRequires:	libgnomeprint-devel >= 2.5.0
BuildRequires:	libgnomeui-devel >= 2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.5.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.5.0
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	xft-devel >= 2.1.2
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	libbonobo >= 2.5.0
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

%build
%{__libtoolize}
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%post
%gconf_schema_install
/usr/bin/scrollkeeper-update

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/eog-image-viewer
%attr(755,root,root) %{_libdir}/eog-collection-view
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/idl/*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
