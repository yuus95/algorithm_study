# algorithm_study

## 규칙

- 8시 50분 에이바우트 

- 문제 2개풀기

- 1문제당 문제 푸는시간 45분 답지보고 푸는시간 20분 설명하는시간 10분

- 다음주 문제 선정 후 스터디 오기전에 개념 공부하기

<br>

## 카카오 문제풀이 여부 체크
|  년도              | 1번|2번|3번|4번|5번|6번|7번                                          | 링크     |
| ------------------ | --|--|--|--|--|--|------------------------------------- | -------- |
| 2021 |✅|✅|✅|✅|✅|||[링크](https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/)|
| 2020 |✅|✅|✅|||||[링크](https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/)|
| 2019 |✅|✅|✅|✅||||[링크](https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/)|


### 아이마스 모빌리티 면접

- 간단한 자기소개

  - 안녕하세요 개발과 성장에 관심이 많은 취준생 26살 김승욱 입니다. 저는 XXX에 들어가기 위해서 두가지를 준비했습니다.
  - 첫번째는 실무역량입니다. 저는 컴퓨터공학과를 졸업하고 실무역량이 부족하다고 생각되어 부트캠프에 지원하여서  SpringBoot에 대한 내용과 협업에 대해 배워서 XXX에 들어가게되면 빠르게 적응할 수 있다고 생각합니다.
  - 두번째는 성장가능성입니다. 저는 현재 공부한 내용을 블로그에 기록하고 있고 단순히 기능 구현에만 의미를 두는게 아니라 어떻게 하면 더 효율적인 코드를 짤 수 있을지에 대해서 고민하고 개선하기 위해 노력하여 더욱 성장 가능할 것이라고 생각합니다.

- OOP에 대해서 설명해주세요

  - 프로그래밍에서 필요한 데이터를 추상화시켜 상태와 행위를 가진 객체를 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직을 구성하는 프로그래밍 방법입니다.

- 객체지향 프로그래밍 키워드

  - 추상화 : 불필요한 정보는 숨기고 중요한 정보만을 표현함으로써 공통의 속성이나 기능을 묶어 이름을 붙이는 것
  - 캡슐화 : **기능과 특성의 모음을 "클래스"라는 "캡슐"에 넣어서 분류해서 넣는 것**이 캡슐화다.
  - 상속 : **상속**은 부모클래스의 속성과 기능을 그대로 이어받아 사용할 수 있게하고 기능의 일부분을 변경해야 할 경우 상속받은 자식클래스에서 해당 기능만 다시 수정(정의)하여 사용할 수 있게 하는 것이다. **다중 상속은 불가하다.**
  - 다형성 : 하나의 변수명, 함수명 등이 상황에 따라 다른 의미로 해석될 수 있는 것이다.
    즉, 오버라이딩(Overriding), 오버로딩(Overloading)이 가능하다는 얘기다.
    - **오버라이딩** : 부모클래스의 메서드와 같은 이름, 매개변수를 재정의 하는 것.
    - **오버로딩** : 같은 이름의 함수를 여러 개 정의하고, 매개변수의 타입과 개수를 다르게 하여 매개변수에 따라 다르게 호출할 수 있게 하는 것. (return 타입은 상관없다.)

- Object에 대해서 설명해주세요

  - 객체란, 소프트웨어 세계에 구현할 대상
  - 클래스의 인스턴스 라고도 부른다. OOP 관점에서 클래스의 타입으로 선언되었을 때 객체라고 부른다.
  - 객체는 현실 세계에 가깝고, 인스턴스는 소프트웨어 세계에 가깝다.

- 클래스

  - 연관되어 있는 변수와 메서드의 집합
  - 클래스란, 객체를 만들어 내기 위한 설계도 혹은 틀

- 인스턴스

  - 객체를 소프트웨어에 실체화 하면 그것을 인스턴스 라고 부른다.
  - OOP의 관점에서 객체가 메모리에 할당되어 실제 사용될 때 인스턴스 라고 부른다.
  - 객체는 클래스의 인스턴스이다.

  ![image-20210531192153864](C:\Users\rlatm\AppData\Roaming\Typora\typora-user-images\image-20210531192153864.png)

- 인스턴스화 된다라는게 무슨의미인가여

  - 클래스로부터 객체를 만드는 과정을 클래스의 인스턴스화(instantiate)라고 한다.

    어떤 클래스로부터 만들어진 객체를 그 클래스의 인스턴스(instance)라고 한다.

- String, StringBuffer, StringBuilder 차이점이 무엇인가요

  - 첫번째 차이점은 String은 불변하다는 특징을 가지고 있어서 수정을 하지못하고 새로운 String 인스턴스가 생성되고 전에 있던 String은 GC에 의해 사라지게 된다. 그래서 좋은 성능을 기대하기는 힘들다. (String 불변, StringBuffer, StringBuilder 가변)
  - **StringBuffer**는 동기화 키워드를 지원하여 **멀티쓰레드 환경에서 안전하다는 점(thread-safe)** 입니다. 참고로 **String**도 불변성을 가지기때문에 마찬가지로  **멀티쓰레드 환경에서의 안정성(thread-safe)**을 가지고 있습니다.  
  - 반대로 **StringBuilder**는 동기화를 지원하지 않기때문에 멀티쓰레드 환경에서 사용하는 것은 적합하지 않지만 동기화를 고려하지 않는 만큼 단일쓰레드에서의 성능은 StringBuffer 보다 뛰어납니다

- 프로세스란?

  - 운영체제로부터 시스템 자원을 할당받는 작업의 단위
  - 하나의 프로세스는 크게 코드영역(code), 데이터 영역(date), 스택 영역(stack), 힙 영역(heap) 4가지로 이루어져 있습니다.

- 스레드란?

  - 한 프로세스 내에서 동작되는 여러 실행의 흐름, 프로세스 하나에 자원을 공유하면서 일련의 과정을 여러 개를 동시에 실행 시킬 수 있다.

- 멀티프로세스

  - 장점 : 안정성이 높다 (독립된 구조기 때문에)
  - 단점 : 여러 프로세스를 왔다갔다 하는 컨텍스트 스위칭으로 인한 성능저하

- 멀티쓰레드

  - 장점 : 응답시간 단축, 자원소모 감소
  - 단점 : 미묘한 시간차나 변수 공유함으로써 오류 발생 가능

- MVC에 대해서 설명해주세요

  - MVC 패턴은 Model, View, Controller 이 3가지로 나뉘어 역할을 분할하여 처리한다.

    역할을 나누어 처리하기 때문에 서로의 결합도가 낮아져서 좋은 코드가 되며 유지보수도 하기 편해진다.

- JPA에서 Entity를 설계할때 주의점을 말해주세요

  - Entity에는 가급적 Setter를 사용하지 말 것

    - Entity가 영속성이 유지되는 도중 수정되면 그 값은 DB에 그대로 반영됩니다.
      그런데 Setter를 열어두고 값을 변경하는 경우에는 변경 포인트가 많아 유지보수가 어려워 질 수 있습니다.

  - 모든 연관관계는 지연로딩으로 설정한다

    - 즉시로딩(EAGER)를 사용 할 경우, 어떤 SQL이 나갈지 추적하기 어렵다

  - 컬렉션은 필드에서 바로 초기화하자

  - #### Entity는 최대한 순수하게 유지해야한다!!!

- DTO를 사용하는 이유

  - 순환참조를 예방할 수 있다.
    - JPA로 개발할 때, 양방향 참조를 사용했다면 순환참조를 조심해야한다.
  - 엔티티 내부 구현을 캡슐화 할 수 있다.
  - **DB Layer와 View Layer 사이의 역할을 분리 하기 위해서**다

- N+1 문제에 대해 짧게 설명해주세요

  - Lazy 로딩에 의해서 한번에 모든 정보를 안가져와서 발생하는 문제인데 폐치조인을 사용해서 해결할 수 있다.

  - SQL 1번으로 100명의 회원을 조회하였는데,

    각 회원마다 주문한 상품을 추가로 조회하기 위해 100번의 SQL을 추가로 실행하는 상황을 말한다.

    **한번 SQL을 실행해서 조회된 결과 수만큼 N번 SQL을 추가로 실행**한다고 해서 N+1 문제라 한다.

- 생성자 injection을 사용한 이유

  - 필드 인젝션은 점차 테스트 코드의 중요성이 부각됨에 따라 필드의 객체를 수정할 수 없는 필드주입은 사용하지 않는것이 좋다. 또한 필드 주입은 반드시 DI 프레임워크가 존재해야 하므로 반드시 사용을 지양해야 한다.

    ![image-20210531183310671](C:\Users\rlatm\AppData\Roaming\Typora\typora-user-images\image-20210531183310671.png)

  - 생성자 인젝션은 생성자로 객체를 생성하는 시점에 필요한 빈을 주입한다. 그러므로 순환참조를 해결 할 수 있다. 필드를 final로 선언 가능하다. DI 컨테이너를 사용하지 않고도 테스트를 진행 할 수 있다.

    ![image-20210531183851052](C:\Users\rlatm\AppData\Roaming\Typora\typora-user-images\image-20210531183851052.png)



---

# 뉴플로이 면접

개발자를 왜 선택했는지

성격 장단점

항해99 하면서 힘들었던점

기술적인 부분 말고 자기소개부분?만 물어봄

---

# 태피툰 면접

- 자바 람다 관련  함수형 프로그래밍
  - 함수형 프로그래밍은 명령형이 아닌 선언적 방식으로 구현되며 흐름 제어를 명시적으로 기술하지 않고 프로그램 로직이 표현된다는 것을 의미한다.
  - 람다는 함수의 구조로 되어있고 -> 와 같이 화살표 형태의 기호를 이용해 매개변수를 함수 바디로 전달하는 형태

- 객체지향프로그래밍 장점, 단점
  - 장점 : 재사용성, 생산성 향상
  - 단점 : 개발속도 느림, 실행속도 느림

- 가비지컬렉션이란?
  - C/C++ 언어와 달리 자바는 개발자가 명시적으로 객체를 해제할 필요가 없습니다. 자바 언어의 큰 장점이기도 합니다. 사용하지 않는 객체는 메모리에서 삭제하는 작업을 Gargabe Collection(GC)라고 부르며 JVM에서 GC를 수행합니다. 

- 자바 컬렉션 List, set, map에 대한 설명
  - List : 순서가 있는 데이터의 집합으로 데이터의 중복을 허용한다.
  - Set : 순서를 유지하지 않는 데이터의 집합으로 데이터의 중복을 허용하지 않는다.
  - Map : 키, 값으로 이루어진 데이터의 집합으로, 순서는 유지되지 않으며 키의 중복을 허용하지 않으나 값의 중복은 허용한다.

- 스프링 자세하게 DI에 대한 설명, 생성자 injection이 좋은 이유
  - 필드주입을 사용하게 되면 배터리 일체형 핸드폰과 같다고 볼 수 있다 반면에 setter와 생성자 주입은 분리형으로 볼 수 있어 조금 더 유연하다

- 테스트 코드에 대한 설명??
  - 단위테스트를 사용하면 좋은점은 개발 초기에 문제를 발견할 수 있다.

- ORM에 대한 설명
  - ORM이란 객체와 DB테이블이 매핑을 이루는 것을 말한다. 즉 객체가 테이블이 되도록 매핑 시켜주는 것을 말함
  - **ORM을 이용하면 SQL Query가 아닌 직관적인 코드(메서드)로서 데이터를 조작**할 수 있습니다.

- JPA 장점, 단점(동적쿼리?)
  - JPA란 자바 ORM 기술에 대한 API 표준 명세를 의미한다.
  - Hibernate는 JPA라는 명세의 구현체이다.
  - 장점
    - 생산성 : SQL의 반복작업이 없어진다.
    - 유지보수 : 테이블 컬럼 한개가 바뀌면 Mybatis에서는 관련 DAO의 파라미터, 결과 SQL등을 모두 확인하여 수정해주어야한다. JPA는 대신 해준다.
  - 단점
    - 성능 : 직접 SQL을 호출 하는 것보다 성능이 떨어 질 수 있다.
    - 세밀함 : 복잡한 통계 분석 쿼리를 메서드 호출로 처리하기 힘들다. (이러한 문제를 보완하기 위해 JPA에서 JPQL을 지원한다.)



---

# 핵클 면접

모르는게 있더라도 내 경험에서 이러이러할것 같다고 말하기 (틀리더라도)

- 생성자 주입 사용시 장점

  - 순환 참조 방지
    - 순환 참조는 A -> B를 참조하면서, B -> A를 참조하는 경우 발생하는 문제
    - 생성자 주입은 먼저 빈을 생성하지 않고 주입하려는 빈을 찾는다. 그래서 실행시 바로 순환참조 에러가 뜨면서 찾을 수 있다.
  - final 선언이 가능
    - 생성자 주입 시, 의존성 주입이 클래스 인스턴스화 중에 시작되므로 final을 선언할 수 있다. 따라서 객체를 변경 불가능하게 할 수 있다.
  - 테스트 코드 작성 용이
    - 스프링 컨테이너 도움 없이 테스트 코드를 더 편리하게 작성 가능

- MVC 진행 방식

  - 클라이언트로부터 요청이 들어오면 dispatcherServlet이 가장 먼저받는다.
  - HandlerMapping이 요청 URL과 매핑되는 Controller 검색 후 리턴
  - HandlerAdapter에서 알맞은 controller 처리요청
  - ViewResolver에서 controller가 리턴한 view 검색후 view를 클라이언트로 보냄

  ![image-20210603192513707](C:\Users\rlatm\AppData\Roaming\Typora\typora-user-images\image-20210603192513707.png)

- AOP

  - 관점 지향 프로그래밍, 어떤 로직을 기준으로 핵심적인 관점, 부가적인 관점으로 나누어서 보고 그 관점을 기준으로 각각 모듈화 하겠다는 것이다.
  - 스프링 빈에만 AOP 적용 가능

- 프록시

  - 프록시는 타겟을 감싸서 타겟의 요청을 대신 받아주는 랩핑 오브젝트이다.
  - 프록시의 단어 자체로는 '대리인'이라는 의미를 내포하고 있음. 스프링 AOP에서의 프록시란 말그대로 대리하여 업무를 처리. 함수 호출자는 주요 업무가 아닌 보조 업무를 프록시에게 맡기고, 프록시는 내부적으로 이러한 보조 업무를 처리.

- 필터에 대한 동작 방식

  - Interceptor와 Filter는 Servlet 단위에서 실행된다.  반면 AOP는 메소드 앞에 Proxy패턴의 형태로 실행된다.

    ![image-20210603201501026](C:\Users\rlatm\AppData\Roaming\Typora\typora-user-images\image-20210603201501026.png)

- spring security

  - 스프링 기반의 어플리케이션의 보안(인증과 권한)을 담당하는 프레임워크이다.

  - 세션-쿠키 방식으로 인증한다.

    ![image-20210603201942553](C:\Users\rlatm\AppData\Roaming\Typora\typora-user-images\image-20210603201942553.png)

- jwt

  - JWT 방식은 확장성에 큰 강점을 가진다. 만약 세션을 사용하는 경우, 서버를 확장할 때마다 각 서버에 세션 정보를 저장하게 된다. 이렇게 될 경우, 특정 서버에서 로그인 인증을 받을 때 다른 서버에서는 로그인을 했는지 알 수 없다는 단점이 있다.

- OAuth2 

  - OAuth (OpenID Authentication) 란, 타사의 사이트에 대한 접근 권한을 얻고 그 권한을 이용하여 개발할 수 있도록 도와주는 프레임워크다. 구글, 카카오, 네이버 등과 같은 사이트에서 로그인을 하면 직접 구현한 사이트에서도 로그인 인증을 받을 수 있도록 되는 구조다.

  - OAuth2 로그인을 사용한다면 `UsernamePasswordAuthenticationFilter` 대신 `OAuth2LoginAuthenticationFilter` 가 호출되게 해야한다.

  - oauth는 세션대신 토큰을 사용하여 인증 진행 (토큰을 또 jwt 토큰으로 바꿔서 사용 많이함) 

  - 인증(Authentication)은 유저가 누구인지 확인하는 절차, 인가(Authorization)는 유저에 대한 권한을 확인한다.

    ![image-20210523010103239](C:\Users\rlatm\AppData\Roaming\Typora\typora-user-images\image-20210523010103239.png)

- JPA, ORM 객체와 데이터베이스 차이 매꿔주는 이론 정확히 알기

  - ORM은 객체와 디비의 데이터를 자동으로 매핑해준다.

- 영속성 컨텍스트란, 영속성 컨텍스트가 있어서 장점

  - 영속성 컨텍스트는 엔티티를 영구 저장하는 환경이라는 뜻이다. EntityManager는 영속성 컨텍스트에 Entity를 보관하고 관리
  - 영속성 컨텍스트 장점
    - 1차캐시 (First Level Cache) : 1차캐시에서 데이터를 먼저 찾고 없으면 DB에서 찾는다.
    - 동일성 보장 (Identify) : 동일한 @id 값으로 검색한 엔티티는 동일성을 보장해준다.
    - 쓰기 지연 (Write-behind) : 
      - 트랜잭션을 커밋하기 직전까지 쿼리를 날리지 않고 영속성 컨텍스트에 보관한다. 트랜잭션이 커밋되지 않거나 중간에 의도치않은 익셉션 발생시 롤백하여 DB에 영향이 없다.
      - 한 트랜잭션안에서 여러번 `persist` 메소드를 호출하여 DB에 저장을 시도할 때 `persist` 함수가 호출된 시점이 아닌 트랜잭션이 커밋되는 시점에 한번에 쿼리날린다.
    - 변경 감지 (Dirty Checking) : 스냅샷을 이용하여 영속성 컨텍스트에 저장된 엔티티는 변경이 일어나면 자동으로 데이터베이스 에서 수정된다.
    - 지연 로딩 (Lazy Loding): 실제 객체 대신 프록시 객체를 로딩해두고 해당 객체를 실제 사용할 때 영속성 컨텍스트를 통해 불러오는 방법

- servlet dispacher

  - controller로 들어가기 전에 맨 앞에서 모든 요청을 받아서 해당하는 controller로 보내준다.

- 트랜잭션

  - 어떤 일련의 작업들은 모두 에러 없이 끝나야 하며, 

    만약 중간에 에러가 발생 한다면, 에러 발생 이전 시점까지 작업되었던 내용은 모두 원상복구 되어야 합니다.

- 객체지향 관점에서 스프링 프레임워크를 바라봤을 때 장단점

  - 스프링이 지향하는 목적 정의 : POJO 프로그래밍

- POJO(Plain Old Java Object)는 말 그대로 간단한 자바 오브젝트를 사용하는 것을 말한다.

  - 진정한 POJO란 객체 지향적인 원리에 충실하면서, 환경과 기술에 종속되지 않고 필요에 따라 재활용될 수 있는 방식으로 설계된 오브텍트를 말한다. 
  - 스프링에 IOC/DI, AOP는 POJO 프로그래밍을 손쉽게 할 수 있도록 지원하는 기술이다.

- 브라우저에서 URL을 입력했을때 일어나는 일들

  - 프로토콜, URL, 포트를 해석한다.
  - HSTS 목록 조회
    - HSTS(HTTP Strict transport security) : HTTP를 허용하지 않고 HTTPS를 사용하는 연결만 허용하는 기능
    - 그리고 자신의 HSTS캐시에 해당 URL을 저장하는데 이를 HSTS 목록이라고 부릅니다.
  - URL을 IP주소로 변환
    - DNS 서버로 요청
  - 라우터를 통해 해당 서버의 게이트웨이까지 이동
    - DNS서버에게 IP주소를 받았으니 이제 해당 서버로 요청을 보냅니다.
  - ARP를 통해 IP주소를 MAC주소로 변환
    - 실질적인 통신을 하기 위해서는 논리 주소인 IP주소를 물리 주소인 MAC 주소로 변환해야 합니다.
  - 대상 서버와 TCP 소켓 연결
    - 이제 대상 서버와 통신하기 위해 TCP 소켓 연결을 진행합니다. 소켓 연결은 3-way-handshake라는 과정을 통해 이루어집니다.
  - HTTP(HTTPS) 프로토콜로 요청, 응답
    - 이제 연결이 확정되었으니 드디어 해당 페이지 **www.daum.net**를 달라고 서버에게 요청합니다.
  - 브라우저에서 응답을 해석
    - 서버에서 응답한 내용은 HTML, CSS, Javascript 등으로 이루어져 있습니다
