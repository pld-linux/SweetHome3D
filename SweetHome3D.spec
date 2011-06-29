#
# TODO:	- use system java3d (it's GPL now), maybe other libs too
#	- build and package applet
#	- libCG*.so isn't required, package shouldn't provide libj3dcore-ogl*.so
#
Summary:	An interior design application
Name:		SweetHome3D
Version:	3.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/sweethome3d/%{name}-%{version}-src.zip
# Source0-md5:	73ae64a8d5cfd418df79619d4b792ea9
URL:		http://www.sweethome3d.com/
BuildRequires:	ant
BuildRequires:	java-sun
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interior design application.

%prep
%setup -q -n %{name}-%{version}-src
%{__sed} -e 's#exec "$PROGRAM_DIR"/jre1.6.0_23/bin/java#env java#g; 3,8 c\PROGRAM_DIR=%{_javadir}/SweetHome3D' \
	-e 's#:"$PROGRAM_DIR"/jre1.6.0_23/lib/javaws.jar#:%{_jvmlibdir}/java/jre/lib/javaws.jar#' -i install/linux/SweetHome3D
#	-e 's/$1/"$1"/' \

%build
%ant application furniture textures help

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}/%{name}/lib}

install install/linux/%{name} $RPM_BUILD_ROOT%{_bindir}
install -p build/*.jar lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/lib
%ifarch %{ix86}
install -p lib/linux/i386/libj3dcore-ogl*.so $RPM_BUILD_ROOT%{_javadir}/%{name}/lib
%endif
%ifarch %{x8664}
install -p lib/linux/x64/libj3dcore-ogl.so $RPM_BUILD_ROOT%{_javadir}/%{name}/lib
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT THIRDPARTY-LICENSE-*.TXT
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}
