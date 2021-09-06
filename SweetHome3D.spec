#
# TODO:	- use system java3d (it's GPL now), maybe other libs too
#	- build and package applet
#
Summary:	An interior design application
Summary(pl.UTF-8):	Aplikacja do projektowania wnętrz
Name:		SweetHome3D
Version:	6.4.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/sweethome3d/%{name}-%{version}-src.zip
# Source0-md5:	488847dfe26fb099feec7d10ce154dcd
URL:		http://www.sweethome3d.com/
BuildRequires:	ant
BuildRequires:	jdk >= 1.5
BuildRequires:	sed >= 4.0
# because of binary libs
ExclusiveArch:	%{ix86} %{x8664}
ExcludeArch:	i386 i486
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interior design application.

%description -l pl.UTF-8
Aplikacja do projektowania wnętrz.

%prep
%setup -q -n %{name}-%{version}-src

%{__sed} -e 's#exec "$PROGRAM_DIR"/jre8/bin/java#env java#; 3,8 c\PROGRAM_DIR=%{_javadir}/SweetHome3D' \
	-e 's#jogl-java3d.jar#&:"$PROGRAM_DIR"/lib/java3d-1.6/jogl-all.jar#' \
	-e 's#:"$PROGRAM_DIR"/jre8/lib/javaws.jar#:%{_jvmlibdir}/java/jre/lib/javaws.jar#' -i install/linux/SweetHome3D

%build
%ant application furniture textures help

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}/%{name}/lib/java3d-1.6}

install install/linux/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -p build/*.jar lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/lib
%{__rm} $RPM_BUILD_ROOT%{_javadir}/%{name}/lib/{j3dcore,j3dutils,vecmath}.jar
cp -p lib/java3d-1.6/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/lib/java3d-1.6

%ifarch %{ix86}
install -p lib/java3d-1.6/linux/i586/*.so $RPM_BUILD_ROOT%{_javadir}/%{name}/lib/java3d-1.6
%endif
%ifarch %{x8664}
install -p lib/java3d-1.6/linux/amd64/*.so $RPM_BUILD_ROOT%{_javadir}/%{name}/lib/java3d-1.6
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT THIRDPARTY-LICENSE-*.TXT
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}
