Name     : jdk-jackson-module-scala
Version  : 2.7.6
Release  : 2
URL      : http://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-scala_2.11/2.7.6/jackson-module-scala_2.11-2.7.6.jar
Source0  : http://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-scala_2.11/2.7.6/jackson-module-scala_2.11-2.7.6.jar
Source1  : http://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-scala_2.11/2.7.6/jackson-module-scala_2.11-2.7.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jackson-module-scala_2.11.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jackson-module-scala_2.11.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jackson-module-scala_2.11.xml \
%{buildroot}/usr/share/maven-poms/jackson-module-scala_2.11.pom \
%{buildroot}/usr/share/java/jackson-module-scala_2.11.jar

%files
%defattr(-,root,root,-)
/usr/share/java/jackson-module-scala_2.11.jar
/usr/share/maven-metadata/jackson-module-scala_2.11.xml
/usr/share/maven-poms/jackson-module-scala_2.11.pom
