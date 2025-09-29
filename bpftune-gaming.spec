# BPF-based auto-tuning SPEC file

%define name        bpftune
%define release     {?dist}
%define version     0.2
%define _unpackaged_files_terminate_build 0
%global _unitdir    /usr/lib/systemd/system/
%global commit c2b481e9c45e38d39d46c627296177fd803e307b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Small Makefile change
Patch:		https://patch-diff.githubusercontent.com/raw/oracle/bpftune/pull/130.patch

License:        GPLv2 WITH Linux-syscall-note
URL:		https://github.com/shanefagan/bpftune
Source:		%{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

Name:           %{name}
Summary:        BPF/tracing tools for auto-tuning Linux
Group:          Development/Tools
Requires:       libbpf >= 0.6
Requires:       libnl3
Requires:       libcap
BuildRequires:  libbpf-devel >= 0.6
BuildRequires:  libcap-devel
BuildRequires:	bpftool >= 4.18
BuildRequires:  libnl3-devel
BuildRequires:  clang >= 11
BuildRequires:  clang-libs >= 11
BuildRequires:  llvm >= 11
BuildRequires:  llvm-libs >= 11
BuildRequires:	python3-docutils
Version:        %{version}
Release:        %{release}
Prefix:         %{_prefix}

%description
Service consisting of daemon (bpftune) and plugins which
support auto-tuning of Linux via BPF observability.

%prep
%setup -q -n bpftune-%{commit}

%build
make

%install
rm -Rf %{buildroot}
%make_install

%files
%defattr(-,root,root)
%{_sysconfdir}/ld.so.conf.d/libbpftune.conf
/usr/sbin/bpftune
%{_unitdir}/bpftune.service
%{_libdir}/libbpftune.so.%{version}.%{rel}
%{_libdir}/bpftune/*
%{_mandir}/*/*

%changelog
* Wed Mar 26 2025 Alan Maguire <alan.maguire@oracle.com> - 0.2-1
- Add support for PCP PMDA package
* Tue May 30 2023 Alan Maguire <alan.maguire@oracle.com> - 0.1-3
- Fix timeout retry logic in libbpftune. [Orabug: 35385703]
* Wed May 24 2023 Alan Maguire <alan.maguire@oracle.com> - 0.1-2
- Spec file reviewed.
* Mon May 30 2022 Alan Maguire <alan.maguire@oracle.com> - 0.1-1
- Initial packaging support
