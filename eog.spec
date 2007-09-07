Summary:	The Eye of GNOME image viewer
Summary(pl.UTF-8):	Oko GNOME - przeglądarka obrazków
Summary(pt_BR.UTF-8):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	2.19.92
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/eog/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	773960d53b71b4e3c539c139db3bd277
Patch0:		%{name}-codegen.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-icon-theme >= 2.19.91
BuildRequires:	gnome-desktop-devel >= 2.19.90
BuildRequires:	gnome-vfs2-devel >= 2.19.91
BuildRequires:	intltool >= 0.36.1
BuildRequires:	lcms-devel
BuildRequires:	libart_lgpl-devel >= 2.3.19
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeprintui-devel >= 2.18.0
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires:	libgnomeui >= 2.19.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl.UTF-8
Eye of GNOME (Oko GNOME) jest narzędziem do oglądania/katalogowania
obrazków.

%description -l pt_BR.UTF-8
Aplicativo para visualizar imagens chamado Eye of GNOME.

%package devel
Summary:	Header files for eog
Summary(pl.UTF-8):	Pliki nagłówkowe eog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for eog.

%description devel -l pl.UTF-8
Pliki nagłówkowe eog.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__gnome_doc_common}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install eog.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall eog.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/eog.schemas
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/eog-2.20
%{_pkgconfigdir}/*.pc
