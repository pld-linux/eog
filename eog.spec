Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przeglądarka obrazków
Summary(pt_BR):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	2.3.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	e977cd54572ad0cf944022591c89e650
Patch0:		%{name}-libtool.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.3.3
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.3.1-4
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	libgnomeprint-devel >= 2.2.1
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.2.1
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	xft-devel >= 2.1.2
BuildRequires:	eel-devel >= 2.3.3
Requires:	libbonobo >= 2.3.1-4
Requires(post): GConf2
Requires(post): scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl
Eye of GNOME (Oko GNOME) jest narzędziem do oglądania/katalogowania
obrazków.

%description -l pt_BR
Aplicativo para visualizar imagens chamado Eye of GNOME.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
sed -e 's/-ourdir/ourdir/' xmldocs.make >xmldocs.make.tmp
mv xmldocs.make.tmp xmldocs.make
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}

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
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/idl/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
