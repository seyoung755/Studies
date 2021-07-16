# 1. Gradle 프로젝트를 Springboot 프로젝트로 만들기
## build.gradle 
```java
buildscript {
    ext {
        springBootVersion = '2.1.7.RELEASE'
    }
    repositories {
        mavenCentral()
        jcenter()
    }
    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
    }
    }

apply plugin: 'java'
apply plugin: 'eclipse'
apply plugin: 'org.springframework.boot'
apply plugin: 'io.spring.dependency-management'


group 'com.seyeong.tutorial'
version '1.0-SNAPSHOT'

sourceCompatibility = 1.8

repositories {
    mavenCentral()
    jcenter()
}

dependencies {
    compile('org.springframework.boot:spring-boot-starter-web')
    testCompile('org.springframework.boot:spring-boot-starter-test')
}
```

# 2. 의존성 주입
- 의존성 주입(Dependency Injection)이란?

: 어떤 객체가 사용할 객체를 직접 만드는 것이 아니라 외부에서 생성하여 연결한다 

  누가? Spring이 해준다

  왜? 객체를 직접 만들어 사용하면 의존성이 높은 객체가 생기고 결과적으로 코드의 재활용성이 떨어진다. 

(수정사항이 발생하면 결합된 모든 클래스를 수정해야 하기 때문이다.)
  
  즉, 의존성 주입을 통해 코드의 재활용성이 높아지고 단순화된 코드를 짤 수 있다.
  
  Spring은 Bean을 통해 객체를 관리하여 주입해줌으로써 의존성 주입을 구현한다. 
  
  Bean으로 등록하는 방법은 어노테이션을 통해 등록한다.
  
  - @Bean, @Component, @Controller, @Service, @Repository 등이 있으며 자세한 차이는 아래 자료를 참조한다. 
  - 
  ![image](https://user-images.githubusercontent.com/54302155/125612440-e3c5c8ee-9031-4f57-9b91-de2ef092f2a9.png)   
  출처 : https://blog.naver.com/dmswo106/222263419897   
  
  Bean을 주입받는 방식은 크게 필드 주입, Setter 주입, 생성자 주입으로 나뉜다.
  
  1. 필드 주입    
  예시)   
  ```java
  @Controller
  public class MemberController {
    @Autowired // Spring bean에 등록된 MemberService 객체를 가져다 주입해준다.
    private MemberService memberService;
  ```  
  - 필드 주입은 가장 간결한 방법이지만 순수한 자바코드로 테스트하기 힘들다는 단점으로 잘 사용하지 않는다.

  2. Setter 주입   
  예시)
  ```java
  @Autowired
  public void setOwners(OwnerRepository r) {
  this.owners = r;
  }
  ```   
  - Setter 주입은 현재 권장되지 않는 방식임

  3. 생성자 주입
  예시)
  ```java
  @Controller
  public class MemberController {
  
    private MemberService memberservice;
    
    @Autowired // 생성자가 하나인 경우 생략이 가능하다
    public MemberControlle(Memberservice memberService) {
        this.memberService = memberService;
    }
    
  }
  ```
  생성자 주입이 가장 권장되는 방법인 이유   
   - 순환 참조를 방지할 수 있다.   
    : 생성자 주입은 생성자로 객체를 생성하는 시점에 필요한 빈을 주입한다. 즉, 생성자의 인자에 사용되는 빈을 찾거나 만든    후 그 빈으로 주입하려는 빈의 생성자를 호출한다. 
    그러나, 다른 주입방식은 빈을 먼저 만든 후에 빈을 찾아서 주입하는 방법이다. 
    즉, 빈을 먼저 생성하고 필드에 대해서 주입하는 방법인 경우에 순환 참조가 발생하여도 에러가 생기지 않아 문제를 파악하기 힘들다.
    
   - 의존관계 주입은 한번 일어나면 어플리케이션 종료까지 불변성을 지켜야 한다. 만약, 세터주입으로 의존관계를 주입하면, 누군가가 실수로 변경할 수도 있다.
    
   - final을 사용할 수 있다.    
     생성자 주입을 제외한 나머지 주입방식은 모두 생성자 생성이후에 호출되므로 final을 사용할 수 없다. 그러나 생성자 주입 방식은 생성자 생성 단계에서 호출되므로 final을 사용할 수 있어 불변성을 지킬 수 있다. 초기화 이후 객체를 변경할 수 없다. 
  
  #### 의존성 주입으로 인하여 제어의 역전(IoC)를 구현할 수 있다.
  - 객체 관리의 주체가 개발자가 아닌 스프링 컨테이너라는 점이다. 

# 3. Model 설계 시 Private를 쓰는 이유
- 어떤 객체의 값을 직접 접근하여 변화시키는 것은 객체지향과 맞지 않기 때문이다. (즉, 좋은 코드가 아니다.)   
ex) 예를 들어, 사람이라는 Class가 있고 그 안에 배고픔이라는 상태가 존재한다. 이 배고픔을 해결하기 위해서 사람 객체를 생성하고, 사람 객체의 배고픔에 접근해서 값을 바꾸는 것은 현실적이지 않다.   
    갑자기 밥을 먹지도 않았는데 배부른 경우는 현실에 없기 때문이다. 현실을 추상화한 객체지향의 특성에 어긋난다.   
    즉, 올바르게 구현하기 위해서는 배고픔이라는 상태는 Private으로 직접 접근하여 값을 바꿀 수 없고, 클래스 내의 Public 메소드인 eat을 통해서 이 값을 증가시키는 것이 올바르다.
    
# 4. Lombok Annotation이 제대로 작동되지 않을 때
- @Getter 등의 어노테이션을 설정했음에도 get 메소드 실행 시 cannot find symbol이 뜨는 경우
- Build.gradle에 다음 의존성을 추가한다.
```
annotationProcessor('org.projectlombok:lombok')

```

# 5. Request를 받을 때 json 데이터를 받는 과정
- @Requestbody 어노테이션을 통해 body data(JSON)임을 알려주고 Model 객체를 인자로 받는다.
- 그러면 Springboot의 MessageConverter를 통해 Model 내의 인자로 매핑해서 받을 수 있다. 
