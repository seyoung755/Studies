# Spring Security의 로그인

1. 스프링 시큐리티는 로그인 요청이 오는지 지켜보고 있다가 parameter로 전달받은 username과 password를 가로챈다.
2. 그리고 해당 정보를 통해 로그인을 진행한다.
3. 로그인이 완료되면 시큐리티 세션에 유저 정보를 등록한다.
4. 위에서 등록된 정보는 DI를 통해 가져와서 사용이 가능해진다. 
5. 시큐리티 세션에 저장되는 유저 정보는 UserDetails type만 가능하다.
  (1) 즉, User type을 UserDetails로 바꿔서 저장한다.
6. 그리고 password는 해싱되지 않으면 로그인이 되지 않는다.
