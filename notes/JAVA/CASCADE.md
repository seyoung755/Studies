### 게시글을 삭제할 때 댓글이 달려있으면 삭제되지 않는 문제
- Foreign key의 CASCADE 옵션을 설정하지 않았기 때문에 삭제가 되지 않는다.   
- 해결하기 위해 글이 삭제되면 댓글이 삭제되도록 옵션을 설정한다. (CascadeType.REMOVE)
- 더 많은 옵션? => JPA Cascade option 검색
