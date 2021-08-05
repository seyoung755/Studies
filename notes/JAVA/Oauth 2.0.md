## 스프링 시큐리티의 세션
- 서버가 관리하는 세션 안에 시큐리티 세션이 있다.
- 시큐리티 세션에는 Authentication 객체만이 들어갈 수 있다. -> DI가 가능하다.
- Authentication 객체 안에는 UserDetails 객체와 OAuth2User 객체가 들어갈 수 있다.
- UserDetails 객체는 일반적인 로그인을 할 때 만들어진다.
- Google, Facebook 로그인 등을 통하면 OAuth2User 객체가 만들어진다.
- 이 때 Authentication 객체를 접근할 때, Authentication 객체를 형변환하거나, @AuthenticationPrincipal 어노테이션을 통해 접근한다.
- 그런데, 로그인 방식에 따라 객체 타입이 다르므로 각각 처리해줘야 하는 불편함이 생긴다.
- 해결하기 위해, 두 클래스를 모두 Implements한 객체를 만들어(PrincipalDetails) Authentication 객체에 담는다.


## PrincipalDetails 객체의 의의
  1. 시큐리티 세션에 저장된 Authentication 내의 userDetails에는 User 정보가 없다. 즉, 세션 정보를 조회해도 유저정보를 찾을 수 없다.   
     그러므로, userDetails를 implement한 PrincipalDetails를 통해 User정보를 포함하여 저장할 수 있게 한다. 
  2. OAuth로 회원가입한 유저와 분리되는 문제를 해결하기 위해 PrincipalDetails를 OAuth2User 또한 implement 한다.
