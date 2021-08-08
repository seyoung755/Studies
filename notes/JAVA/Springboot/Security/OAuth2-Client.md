## OAuth2-Client 라이브러리
- 스프링에서 공식으로 지원하는 Provider는 Google, Facebook, Github 등이 있다. 
- 우리가 추가하고자 하는 NAVER, KAKAO 등의 비공식 Provider를 사용하기 위해서는 커스텀이 필요하다. 

## Provider 등록
- Application.yml에 아래와 같이 설정한다.
![image](https://user-images.githubusercontent.com/54302155/128639581-2a76ecff-5add-4ad4-9be9-bb7434a94c83.png)
(참고 : [네아로 개발 문서](https://developers.naver.com/docs/login/devguide/devguide.md#%EB%84%A4%EC%9D%B4%EB%B2%84%EC%95%84%EC%9D%B4%EB%94%94%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C))
- 이 때, 스프링 시큐리티에서는 Authorization code grant 방식으로 인증을 진행한다. (참고 : [OAuth2 인증 방식 정리](https://cheese10yun.github.io/oauth2/))
