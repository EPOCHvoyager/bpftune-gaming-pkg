# BPF-based auto-tuning SPEC file

%global _unitdir    /usr/lib/systemd/system/
%global commit c2b481e9c45e38d39d46c627296177fd803e307b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define _unpackaged_files_terminate_build 0

Name:           bpftune
Version:        0.2
Release:        %autorelease

# Small Makefile change
Patch:		https://patch-diff.githubusercontent.com/raw/oracle/bpftune/pull/130.patch

License:        GPLv2 WITH Linux-syscall-note
URL:		https://github.com/shanefagan/bpftune
Source:		%{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

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

%description
Service consisting of daemon (bpftune) and plugins which
support auto-tuning of Linux via BPF observability.

%prep
%autosetup -n bpftune-%{commit}

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
%{_libdir}/libbpftune.so.*
%{_libdir}/bpftune/*
%{_mandir}/*/*

%autochangelog
