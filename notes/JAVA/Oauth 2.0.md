## 스프링 시큐리티의 세션
- 서버가 관리하는 세션 안에 시큐리티 세션이 있다.
- 시큐리티 세션에는 Authentication 객체만이 들어갈 수 있다. -> DI가 가능하다.
- Authentication 객체 안에는 UserDetails 객체와 OAuth2User 객체가 들어갈 수 있다.
- UserDetails 객체는 일반적인 로그인을 할 때 만들어진다.
- Google, Facebook 로그인 등을 통하면 OAuth2User 객체가 만들어진다.
- 이 때 Authentication 객체를 접근할 때, Authentication 객체를 형변환하거나, @AuthenticationPrincipal 어노테이션을 통해 접근한다.
- 그런데, 로그인 방식에 따라 객체 타입이 다르므로 각각 처리해줘야 하는 불편함이 생긴다.
- 해결하기 위해, 두 클래스를 모두 Implements한 객체를 만들어(PrincipalDetails) Authentication 객체에 담는다.
