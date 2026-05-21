Summary:	A forensic tool for recovering files from FAT file systems
Summary(pl.UTF-8):	Narzędzie do odzyskiwania plików z partycji FAT
Name:		fatback
Version:	1.3
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/fatback/%{name}-%{version}.tar.gz
# Source0-md5:	4f1beb13670a7eff5b66cff84e5fd42a
Patch0:		%{name}-build.patch
URL:		http://fatback.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
# Trash BR for configure
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fatback is a tool for undeleting files from FAT file systems.

%description -l pl.UTF-8
Fatback jest narzędziem do odzyskiwania usuniętych plików z systemów
plików FAT.

%prep
%setup -q
%patch -P0 -p1

%build
cp -f /usr/share/automake/config.sub /usr/share/automake/config.guess .
%{__autoconf}
%configure2_13
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
%{_infodir}/*.info*
