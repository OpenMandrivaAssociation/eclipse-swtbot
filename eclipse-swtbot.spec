%{?_javapackages_macros:%_javapackages_macros}
Name:           eclipse-swtbot
Version:        2.2.1
Release:        3.3
Summary:        UI and functional testing tool for SWT and Eclipse based applications
Group:		Development/Java
License:        EPL
URL:            https://www.eclipse.org/swtbot/
Source0:        http://git.eclipse.org/c/swtbot/org.eclipse.swtbot.git/snapshot/org.eclipse.swtbot-%{version}.tar.bz2
Patch0:         drop-source-bundles.patch
BuildRequires:  tycho
BuildRequires:  tycho-extras
BuildRequires:  eclipse-gef
BuildRequires:  eclipse-pde
BuildRequires:  jacoco-maven-plugin
BuildRequires:  cbi-plugins
BuildRequires:  eclipse-license
BuildRequires:  tycho
BuildRequires:  log4j12
BuildArch:      noarch

%description
SWTBot is a Java based UI/functional testing tool for testing SWT and Eclipse
based applications. SWTBot provides APIs that are simple to read and write.
The APIs also hide the complexities involved with SWT and Eclipse. This makes
it suitable for UI/functional testing by everyone, not just developers.

%prep
%setup -q -n org.eclipse.swtbot-%{version}

for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
rm -fr $j
fi
done
%patch0
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId ='target-platform-configuration']"
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.eclipse.tycho:tycho-packaging-plugin

%mvn_package ":*.test" __noinstall
%mvn_package ":*.test.*" __noinstall
%mvn_package ":*.examples" __noinstall
%mvn_package "::jar:sources:"


%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles

%changelog
* Wed Dec 3 2014 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-3
- Build with xmvn.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-1
- Update to upstream 2.2.1 release.

* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-1
- Update to latest upstream version.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to the official release.

* Tue Feb 26 2013 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-0.2.20130226git
- New snapshot removing org.junit4 references.

* Tue Feb 26 2013 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-0.1.20130225git
- Update to 2.1.0 prerelease - compatible with kepler platform.

* Wed Feb 20 2013 Alexander Kurtakov <akurtako@redhat.com> 2.0.5-4.20120802git
- Skip tycho version check.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3.20120802git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 6 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.5-2.20120802git
- Fix review comments.

* Thu Aug 2 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.5-1.gita95f41b7ae6d7790dab36bca982d4b833fd2662d
- Initial package
