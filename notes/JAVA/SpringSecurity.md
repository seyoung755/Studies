# Spring Security의 로그인

1. 스프링 시큐리티는 로그인 요청이 오는지 지켜보고 있다가 parameter로 전달받은 username과 password를 가로챈다.
2. 그리고 해당 정보를 통해 로그인을 진행한다.
3. 로그인이 완료되면 시큐리티 세션에 유저 정보를 등록한다.
4. 위에서 등록된 정보는 DI를 통해 가져와서 사용이 가능해진다. 
5. 시큐리티 세션에 저장되는 유저 정보는 UserDetails type만 가능하다.
  (1) 즉, User type을 UserDetails로 바꿔서 저장한다.
6. 그리고 password는 해싱되지 않으면 로그인이 되지 않는다.

# XSS와 CSRF
1. XSS
- 자바스크립트 공격 ex) 게시글 제목에 script로 alert를 많이 띄우는 공격 등
- NAVER의 lucy를 통하여 막을 수 있다.

2. CSRF
- http://naver.com/admin/point?id=?&point=? 라는 포인트를 적립시키는 주소가 있다고 할 때, 시큐리티 등으로 /admin/** 을 인증이 필요하도록 막아둔다.
- 공격자는 관리자로 하여금 어떤 하이퍼링크 이미지를 통해 위 주소로 접속하게 만든다. (접속 권한이 있는 운영자가 누르도록 유도)
- 막는 방법 첫 번째는 GET 방식을 이용하지 않고 POST 방식을 이용해야 한다.
- 또는 Referrer 검증 -> 같은 도메인 상에서 요청이 들어오지 않는다면 차단하도록 하는 것이다.
- CSRF token을 이용하면 header에 token이 없는 요청에 대해서 모두 방어가 가능하다. 

# Session 값 변경하기
1. 사용자가 로그인 요청을 하면 Authentication filter를 거친다.
2. request body의 username과 password로 UsernamePasswordAuthenticationToken을 만든다.
3. 그 Token을 UserDetailService 를 통해서 DB에 해당 정보의 유저가 있는지 확인한 후 있으면 Authentication이라는 객체를 만든다. 
4. 우리가 만든 loadUserByUsername은 username만 가지고 DB에 조회하고 비밀번호는 따로 스프링이 Encoding한 후 DB와 비교해준다.
5. 그래서 User 정보를 세션의 Security context에 저장한다. 

- 위와 같은 과정으로 세션에 값이 저장되므로, 세션 값을 바꿀 때 임의로 Authentication 객체를 만든다.
- 이 때, 필요한 Token도 직접 만든다. 
- 그 다음 Securitycontext에 접근하여 해당 Authentication 객체로 수정한다. 
