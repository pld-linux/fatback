Summary:	A forensic tool for recovering files from FAT file systems
Summary(pl):	Narzêdzie do odzyskiwania plików z partycji FAT
Name:		fatback
Version:	1.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/fatback/%{name}-%{version}.tar.gz
# Source0-md5:	4f1beb13670a7eff5b66cff84e5fd42a
URL:		http://fatback.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	flex
# Trash BR for configure
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fatback is a tool for undeleting files from FAT file systems.

%description -l pl
Fatback jest narzêdziem do odzyskiwania usuniêtych plików z systemów
plików FAT.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
%{_infodir}/*.info*
