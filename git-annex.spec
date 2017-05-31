# nothing to see here
%global debug_package %{nil}

Name:           git-annex
Version:        6.20170519
Release:        1%{?dist}
Summary:        Manage files with git, without checking their contents into git

License:        GPLv3+
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc
BuildRequires:  stack
BuildRequires:  git-core
BuildRequires:  rsync
# magic
BuildRequires:  file-devel
BuildRequires:  zlib-devel

Requires:       git-core

%description
Git-annex allows managing files with git, without checking the file contents
into git. While that may seem paradoxical, it is useful when dealing with files
larger than git can currently easily handle, whether due to limitations in
memory, time, or disk space.

It can store large files in many places, from local hard drives, to a large
number of cloud storage services, including S3, WebDAV, and rsync, with a dozen
cloud storage providers usable via plugins. Files can be stored encrypted with
gpg, so that the cloud storage provider cannot see your data.
git-annex keeps track of where each file is stored, so it knows how many copies
are available, and has many facilities to ensure your data is preserved.

git-annex can also be used to keep a folder in sync between computers, noticing
when files are changed, and automatically committing them to git and
transferring them to other computers. The git-annex webapp makes it easy to set
up and use git-annex this way.


%prep
%setup -q


%build
stack build --system-ghc


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
cp -p .stack-work/install/*/lts-*/*/bin/* %{buildroot}%{_bindir}
cp -p .stack-work/install/*/lts-*/*/share/man/man1/* %{buildroot}%{_mandir}/man1


%files
%license .stack-work/install/*/lts-*/*/doc/*
%doc CHANGELOG NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}-shell
%{_bindir}/git-remote-tor-annex
%{_mandir}/man1/*


%changelog
* Tue May 30 2017 Jens Petersen <petersen@redhat.com> - 6.20170519-1
- build with stack
