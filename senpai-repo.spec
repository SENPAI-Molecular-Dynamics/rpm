Name:		senpai-repo
Version:	1.0
Release:	1
Summary:	SENPAI Molecular Dynamics official repo files
License:	GPLv3
URL:		https://senpaimd.org
%undefine	_disable_source_fetch
Source0:	https://senpaimd.org/src/%{name}-%{version}-%{release}.tar.gz
Vendor:		SENPAI Molecular Dynamics
BuildArch:	x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%global debug_package %{nil}

%description
The SENPAI molecular dynamics (MD) simulator

%prep
%setup -q -n repo

%build
#Nothing to do

%install
mkdir -p %{buildroot}/etc/senpai/
mkdir -p %{buildroot}/etc/yum.repos.d/
install -m 0644 RPM-GPG-KEY-senpaimd %{buildroot}/etc/senpai/RPM-GPG-KEY-senpaimd
install -m 0644 senpaimd.repo %{buildroot}/etc/yum.repos.d/senpaimd.repo

%post
rpm --import /etc/senpai/RPM-GPG-KEY-senpaimd

%files
%attr(644,root,root) /etc/senpai/RPM-GPG-KEY-senpaimd
%attr(644,root,root) /etc/yum.repos.d/senpaimd.repo

%changelog
* Thu May 05 2022 Sasha Emily Chelsea Murgia <mail@chelsea486mhz.fr> 1.0-1
- Initial RPM release
