Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przegl±darka obrazków
Summary(pt_BR):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	1.1.2
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
Source1:	%{name}.gif
Patch0:		%{name}-am.patch
Patch1:		%{name}-makefile.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel >= 2.1.0-3
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.1.3-3
BuildRequires:	intltool
BuildRequires:	libbonoboui >= 2.1.0
BuildRequires:	libgnomeprint-devel >= 2.1.1
BuildRequires:	libgnomeui >= 2.1.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.1.1
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	Xft-devel >= 2.0-6
Requires:	bonobo-activation >= 2.1.0
Requires(post): GConf2
Requires(post): scrollkeeper
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
rm -f missing
sed -e 's/-ourdir/ourdir/' xmldocs.make >xmldocs.make.tmp
mv xmldocs.make.tmp xmldocs.make
glib-gettextize --copy --force
libtoolize --copy --force
intltoolize --copy --force
aclocal -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--enable-platform-gnome-2
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} 

%find_lang %{name} --with-gnome

%post
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/eog-image-viewer
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/idl/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
