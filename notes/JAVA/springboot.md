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

# 6. Maven이란?
- 프로젝트에 필요한 라이브러리가 있는 경우 ex)ojdbc
    1. Oracle 사이트로부터 jdbc를 다운받는다.
    2. 프로젝트 내의 폴더에 파일을 저장한다.
    3. 해당 파일을 인식할 수 있도록 빌드한다.
    4. Import하여 사용이 가능해진다.
- 그런데 만약 다른 프로젝트가 있다면?
    1. 또 필요한 라이브러리 파일을 다른 프로젝트 내에 저장한다.
    2. 위의 과정을 반복한다.
    3. 결국 두 프로젝트에 중복된 파일을 저장해야 한다.
- 중복을 피하기 위해 두 프로젝트에 라이브러리를 저장하지 않고, 로컬상에 임의의 공용 폴더에 라이브러리를 저장한다.
- 그 다음 각 프로젝트에서 공용 폴더를 연결한 후 빌드한다.
- 이로써, 두 프로젝트 간의 중복은 피할 수 있다.
   
그런데? 만약 배포를 했다고 하자.    
서버 상에는 해당 라이브러리 폴더가 없으므로 다시 위와 같은 작업을 반복해야 한다.   
또, 이외에 추가적인 라이브러리를 다운받을 때마다 각 사이트에서 다운로드 받는 과정을 거쳐야 한다.   

### 해결하기 위해서 중앙 저장소라는 개념을 도입한다.
- 중앙 저장소에 흔히 사용되는 라이브러리(Jsoup, Lombok 등)을 저장해둔다.
- 이 저장소로부터 file을 받기 위해서는 pom.xml(Gradle의 경우에는 build.gradle)에 필요한 file을 기록해둔다. 
- 그럼 Maven(혹은 Gradle 등의 프로젝트 관리도구)가 이 파일을 읽어 자동으로 다운받고(.m2의 repository라는 경로에) 빌드해준다.
- 배포 시에도 pom.xml 파일을 포함하고 Maven을 설치하기만 하면 빌드할 때마다 자동으로 라이브러리를 관리해준다.  

# 7. Lombok 사용법
1. Getter/Setter 사용 시
    - @Getter, @Setter로 해당 메소드를 만들 수 있고, @Data를 사용하면 두 메소드를 모두 만들어준다.

2. Constructor 
    - @AllArgsConstructor 를 사용하면 모든 필드에 대해 생성자를 생성한다.
    - @RequiredArgsConstructor를 사용하면 final이 붙은 필드에 대해서만 생성자를 생성한다.
    - @NoArgsConstructor 는 빈 생성자를 생성한다.

3. Builder
    - 생성자에 @Builder라는 어노테이션을 추가하면 빌더 패턴을 구현할 수 있다.
    - 언제 필요한가?
        ex)객체를 생성할 때, 어느 값은 제외하고 넣고 싶은 경우가 있다. 그런 경우가 생길 때마다 해당 인자를 제외한 생성자가 만들어져 있어야 한다. 
           이런 경우, Builder 패턴을 이용하면 순서를 기억할 필요도 없다.

# 8. Yaml 설정
1. 기존 web.xml, root-context.xml(싱글톤으로 관리), servlet-context.xml(new로 생성하여 사용하는 것들)의 합본
2. 프로젝트에 진입하기 전에 한번 읽고 설정을 한 뒤 프로젝트가 실행됨

- mvc view 설정
  : 파일 return 시 기본 경로인 static 경로에서 리턴할 때는 정적인 파일만 브라우저가 인식할 수 있다.   
  그러므로 동적인 파일을 리턴하기 위해서는 yaml 설정을 통해 view의 경로를 옮겨줄 필요가 있다.   
  그렇게 되면 jsp파일을 Tomcat server가 컴파일하여 브라우저에게 전달하여 브라우저가 인식할 수 있게 된다.
  
# 9. MyISAM vs InnoDB ( 출처 : https://rebeccajo.tistory.com/14)
- 결론부터, 둘의 결정적 차이는 트랜잭션 처리의 유무와 Readonly 작업이 많냐에 따라 각각의 장점이 드러난다.
- InnoDB는 트랜잭션 처리가 필요하고 대용량의 데이터를 다룰 때 유리하다.
- MyISAM은 Readonly 작업이 많은 (즉, SELECT를 많이 하는) DB에 유리하다.
    1. MyISAM
        - 항상 테이블에 ROW COUNT를 가지고 있어 SELECT count(*), SELECT 명령이 빠르다.
        - 풀텍스트 인덱스를 지원하여 검색 엔진과 유사한 방법으로 자연어 검색을 지원한다. 즉, 조회에 강력한 장점을 가지고 있다. 
        - 단, row level locking (더 알아보자)을 지원하지 않아 CRUD 작업 시 전체 Table에 lock이 걸린다. 즉, Transaction 시 대용량 데이터를 다루면 속도가 급격히 느려진다.
        
    2. InnoDB
        - row level locking을 지원하여 대용량 데이터의 CRUD에 유리하다.
        - 단, 풀텍스트 인덱스를 지원하지 않는다. 
- 추가로 두 종류의 스토리지 엔진을 같이 사용할 경우, Join 시 주의가 필요하다 (왜 그럴까?)

# 10. Table 간 연관관계의 주인
- 연관관계의 주인이란? FK를 가진 오브젝트 
예시로 게시글 상세보기 페이지를 생각해보자.   
해당 페이지의 정보를 테이블 혹은 Class 단위로 보면 (게시글 작성자 - User class/table), (제목, 내용 - Board class/table), (댓글 - Reply class/table)이 있다.   
만약, JPA가 아닌 MyBatis 등을 썼다면 위 세가지 테이블을 조인하여 SELECT한 다음 가져올 것이다.    
그러나 ORM 방식을 쓰면, Board table만 SELECT하면 된다. 그것을 구현하려면 아래의 과정을 따른다.   

ex) 자바 프로그램에서 DB에 SELECT * FROM Board where Id = 1; 이라는 쿼리를 날리고 싶다.
JPA를 사용하면 JPA를 통해 쿼리를 날리게 되는데, JPA는 요청을 받으면 Board(id=1) 이 필요하다는 것을 인식한다.
1. 그럼 JPA는 위와 같은 쿼리를 날리는 것이 아니라, 먼저 Board가 들고있는 User 객체 때문에 User 정보를 Join하는 쿼리를 날린다.
2. JPA는 이제 Board와 User를 join한 테이블을 가지게 된다.
3. 그러나, Reply Table 정보는 가져올 수 없다. 그러므로 Board에 추가적으로 Reply object를 포함시킨다.
4. 단, 이 때 게시글 당 User 정보는 하나지만 Reply 정보는 여러 개일 수 있으므로 List 형으로 Object를 받는다. 
5. 그리고 Reply 정보는 Foreign key를 설정할 필요가 없다. 왜냐면 여러개의 댓글이 달리면 ReplyID 값이 여러개가 되기 때문에 1정규화(원자성)이 깨진다. 
6. 여기서, reply의 FK는 reply table에 존재해야 하므로, Mappedby를 통해 FK column이 만들어지는 것을 방지한다. 
7. 그럼 Board table을 SELECT 하는 경우에 user는 한 건, reply는 여러 건이 존재할 수 있다. 
8. 이런 경우에 연관관계가 ManyToOne인 user는 기본 전략이 FetchType.EAGER로 Board table을 SELECT 할 시 무조건 가져온다. 
9. 그러나 reply는 여러 건이므로 필요하지 않으면 가져오지 않는 FetchType.LAZY가 기본전략으로 설정되어 있다. 즉, 무조건 가져오게 하려면 설정을 바꿔줘야 한다. 

# 11. JSON 사용법
ex) 외국인이 서로 소통하려면 각자가 타인의 모국 언어를 알고 있어야 한다. 모든 외국인이 소통하려면 각자의 모국어를 배워야 하는 프로토콜은 옳지 않다.
즉, 모든 사람이 소통 가능한 공용어를 정하여 소통한다. (영어)      

프로그래밍 시에도 서로 다른 프로그래밍 언어끼리 소통하는 중간 언어가 JSON이다.   
@Controller는 받는 데이터를 모두 JSON으로 받아서 JAVA object로 바꾼다.   
응답 시에는 Java object는 JSON으로 바꿔서 응답한다.   

# 12. Dirty Checking
가령, 회원 정보를 수정하는 API를 개발했다고 하자. 입력받은 id 정보로 유저를 조회하고 유저의 정보를 입력받은 정보로 바꿨다. 이 때 마지막에 JPARepository의 save 기능을 통해 update 쿼리를 날린다.   
그러나, @Transactional 어노테이션을 이용하면 save, 즉 update를 명시하지 않아도 DB에 정보가 자동으로 update되는 것을 알 수 있다.   
이 것을 가능하게 해주는 것이 바로 더티 체킹이다. 
### 더티 체킹이란?
1. 영속성 컨텍스트
- 만약 User 객체를 save 한다고 하면 해당 객체는 JPA의 영속성 컨텍스트 내의 1차 캐시에 쌓인다. 이 정보를 DB에 반영하게 된다. 
- 1차 캐시에 user 객체가 저장되는 것을 영속화되었다고 한다. DB에 밀어넣는 것을 flush라고 한다. 
- 단, flush를 진행해도 1차 캐시에는 user가 남아 있다. 이를 SELECT등을 진행할 때 캐시로 사용하여 캐싱효과를 누린다. (DB에 접근하지 않고도 캐시에서 바로 데이터를 찾을 수 있다.)   

- 만약 Update를 하고 싶을 때는? 
    1. 먼저 DB로부터 업데이트할 객체를 SELECT하여 1차 캐시에 영속화한다.   
    2. 수정하는 함수에서 해당 데이터를 가져와서 수정한다.
    3. 이 때, save를 호출하면 1차 캐시에 이미 영속화된 객체가 있으므로 새로 save한 객체와의 차이점을 비교하여 기존 객체를 업데이트 한다음 flush한다.   
    4. 그런데 Transactional을 명시하면 함수 return 시에 자동으로 Commit이 된다.
    5. 수정한 데이터는 영속화되어 있으므로 변경된 데이터를 감지하여 자동으로 DB에 update문을 수행해준다. 이 것이 바로 더티 체킹이다. 

더티체킹의 더 자세한 정보 : https://jojoldu.tistory.com/415

# 13. 스프링의 전통적인 트랜잭션
스프링 시작 과정
1. Tomcat 시작
2. web.xml 읽음
3. context.xml -> DB 연결 테스트
4. 어떤 사용자가 송금 서비스를 request하면 xeb.xml과 필터를 거쳐 요청이 이루어지는데 이 때 Controller에 진입하기 직전에,
    (1) DB 연결 세션이 생성된다
    (2) 트랜잭션 시작
    (3) 영속성 컨텍스트 시작
5. 컨트롤러가 어떤 요청인지 확인하고 서비스로 보낸다.
6. 서비스는 송금보내는 사람과 받는 사람의 데이터를 SELECT하여 영속성 컨텍스트에 객체화한다. 
7. 서비스에서는 응답받은 객체를 가져다 값을 변경한다 (보내는사람의 잔고, 받는사람의 잔고)
8. 컨트롤러는 JSON data를 클라이언트에 전송한다. (혹은 html 화면) 이 때, (4) jdbc를 종료된다 -> (5) 트랜잭션 종료 시 변경을 감지하여 DB에 flush한다. (더티 체킹)
9. (6) 영속성 컨텍스트 종료

### 해당 방식의 문제점을 개선한 방법
(1) Controller 진입 전에 영속성 컨텍스트를 시작한다.   
(2)(3) 서비스를 시작한 후 트랜잭션 시작, jdbc 커넥션 시작   
(4)(5) 서비스 종료 직후 트랜잭션과 jdbc 커넥션을 종료    
(6) 컨트롤러 종료 후 영속성 컨텍스트를 종료한다.    

만약 컨트롤러 종료 전에 영속성 컨텍스트를 종료하면, ManyToOne 전략의 추가정보를 가져올 수 없다. 이 때, Fetch type을 Lazy로 하게 되면 프록시 객체를 들고 오게 된다.
만약 컨트롤러 단계에서 영속성 컨텍스트를 종료하지 않으면, 프록시 객체를 호출하여 추가정보를 들고올 수 있다. 즉, 위의 과정과 같이 컨트롤러 종료 후 영속성 컨텍스트를 종료한다.
프록시 객체를 호출하면 다시 jdbc 커넥션을 실행시키고 실제 데이터를 불러온 뒤 커넥션을 종료한다. 
설정의 true-in-view를 활성화시키면 lazy 로딩이 가능해진다. 
