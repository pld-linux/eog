#
# Conditional build:
%bcond_without	apidocs	# API documentation
%bcond_without	librsvg	# SVG scaling using librsvg

Summary:	The Eye of GNOME image viewer
Summary(pl.UTF-8):	Oko GNOME - przeglądarka obrazków
Summary(pt_BR.UTF-8):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	3.34.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/eog/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	f68762ed4cc6306e52cc8528257adf65
Patch0:		librsvg.patch
URL:		https://wiki.gnome.org/Apps/EyeOfGnome
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	gdk-pixbuf2-devel >= 2.36.5
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.4.0
BuildRequires:	gtk+3-devel >= 3.22.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.16}
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libexif-devel >= 1:0.6.14
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpeas-gtk-devel >= 1.0.0
%{?with_librsvg:BuildRequires:	librsvg-devel >= 2.40.0}
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info >= 0.50
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.42.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	exempi >= 1.99.5
Requires:	gdk-pixbuf2 >= 2.36.5
Requires:	glib2 >= 1:2.54.0
Requires:	gsettings-desktop-schemas >= 3.4.0
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	libexif >= 1:0.6.14
%{?with_rsvg:Requires:	librsvg >= 2.44.0}
Requires:	shared-mime-info >= 0.50
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl.UTF-8
Eye of GNOME (Oko GNOME) jest narzędziem do oglądania i katalogowania
obrazków.

%description -l pt_BR.UTF-8
Aplicativo para visualizar imagens chamado Eye of GNOME.

%package devel
Summary:	Header files for eog
Summary(pl.UTF-8):	Pliki nagłówkowe eog
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.22.0

%description devel
Header files for eog.

%description devel -l pl.UTF-8
Pliki nagłówkowe eog.

%package apidocs
Summary:	Eye of GNOME API documentation
Summary(pl.UTF-8):	Dokumentacja API Eye of GNOME
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Eye of GNOME API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Eye of GNOME.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	-Dgtk_doc=%{?with_apidocs:true}%{!?with_apidocs:false} \
	%{!?with_librsvg:-Dlibrsvg=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/eog/plugins

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/eog
%dir %{_libdir}/eog
%dir %{_libdir}/eog/girepository-1.0
%{_libdir}/eog/girepository-1.0/Eog-3.0.typelib
%dir %{_libdir}/eog/plugins
%attr(755,root,root) %{_libdir}/eog/libeog.so
%{_libdir}/eog/plugins/fullscreen.plugin
%attr(755,root,root) %{_libdir}/eog/plugins/libfullscreen.so*
%{_libdir}/eog/plugins/reload.plugin
%attr(755,root,root) %{_libdir}/eog/plugins/libreload.so*
%{_libdir}/eog/plugins/statusbar-date.plugin
%attr(755,root,root) %{_libdir}/eog/plugins/libstatusbar-date.so*
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/eog.convert
%{_datadir}/glib-2.0/schemas/org.gnome.eog.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.gschema.xml
%{_datadir}/metainfo/eog.appdata.xml
%{_desktopdir}/eog.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.eog.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.eog.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.eog-symbolic.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/eog-3.0
%{_pkgconfigdir}/eog.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/eog
%endif
