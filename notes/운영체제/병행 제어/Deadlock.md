## Deadlock
- 공유 자원을 놓고 서로 다른 주체가 서로가 가진 자원을 기다리면서 진전이 없어지는 상황
- 방지하기 위해서는 공유 자원에 대한 조치가 필요하다

## Semaphores

- Counting Semaphore
- Binary Semaphore (Mutex)

### Bounded-Buffer Problem (Producer - Consumer Problem)

- Shared data : buffer 자체 및 buffer 조작 변수(empty/full buffer의 시작 위치)
- Synchronization variables
    - binary semaphore : 공유 데이터에 접근하는 동안 lock/unlock
    - counting semaphore : buffer의 개수를 센다

## Readers-Writers Problem

- 한 프로세스는 읽는 프로세스, 한 프로세스는 쓰는 프로세스이다.
- 한 process가 DB에 write중일 때, 다른 process가 접근하면 안됨
- read는 동시에 여럿이 해도 됨
- solution
    - Writer가 DB에 접근 허가를 아직 얻지 못한 상태에서는 모든 대기중인 Reader들을 다 DB에 접근하게 해준다
    - Writer는 대기 중인 Reader가 하나도 없을 때 DB접근이 허용된다.
    - 일단 Writer가 DB에 접근 중이면 빠져나갈 때까지 Reader의 접근이 금지된다.

- Shared data
    - DB 자체
    - readcount : 현재 DB에 접근 중인 Reader의 수

- Synchronization variables
    - mutex : 공유 변수 readcount를 접근하는 코드의 mutual exclusion 보장을 위해 사용
    - db : Reader와 Writer가 공유 DB 자체를 올바르게 접근하게 하는 역할

- Starvation 발생 가능
    - Reader가 계속해서 도착하면 writer는 db에 접근할 수 없다.
        - 신호등처럼 일정 시간동안만 Reader를 들여보내고 writer에게 권한을 넘겨주는 방식으로 해결한다.

### Dining-Philosophers Problem

- Synchronization variables
    - semaphore chopsticks[5];
- 철학자는 왼쪽 젓가락과 오른쪽 젓가락을 집으면 밥을 먹고, 밥을 다 먹으면 젓가락을 내려놓고 생각한다.
- 밥을 다 먹기 전에는 젓가락을 내려놓지 않기 때문에 Deadlock이 발생한다.
- 해결 방안
    - 4명의 철학자만을 동시에 테이블에 앉힌다.
    - 젓가락을 두 개 모두 집을 수 있을 때에만 젓가락을 집을 수 있게 한다.
    - 비대칭 : 짝수 철학자는 왼쪽부터, 오른쪽 철학자는 오른쪽부터 얻게 규칙을 정한다.

## Monitor

- 모니터 내에서는 한번에 하나의 프로세스만이 활동 가능
- 프로그래머가 동기화 제약조건을 명시적으로 코딩할 필요가 없어 편리하다
- 프로세스가 모니터 안에서 기다리게 하기 위해 condition variable 사용
    - wait와 signal 연산을 통해 blocked, wake 시킴
    

## Deadlock Problem

- 일련의 프로세스들이 서로가 가진 자원을 기다리며 block된 상태
- Resource
    - 하드웨어나 소프트웨어 자원 모두를 의미한다
    - I/O device, CPU cycle, memory space, semaphore 등
    - 자원의 사용 절차 : Request, Allocate, Use, Release
- 데드락의 발생 조건
    - 상호 배제 (Mutual exclusion) : 매 순간 하나의 프로세스만이 자원을 사용할 수 있음
    - 비선점 (No preemption) : 자원을 보유한 프로세스는 스스로 자원을 내어놓을 때까지 뺏기지 않음
    - 보유 대기 (Hold and wait) : 자원을 기다리는 프로세스는 자기 자원을 내어놓지 않고 계속 기다림
    - 순환 대기 (Circular wait) : 서로 필요한 자원을 가진 프로세스들이 맞물리는 사이클이 형성됨
    

### Resource-Allocation Graph (자원 할당 그래프)

- 프로세스와 자원의 관계를 그래프 형태로 나타내는 방법
- 프로세스의 자원 보유 상태와 요청 상황을 확인할 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3295695-4b1a-4212-9246-e3e5d6e4fa63/Untitled.png)

- 그래프에 Cycle이 존재하면 deadlock일 가능성이 있고, 존재하지 않으면 deadlock이 아니다.

## Deadlock의 처리 방법

- Deadlock Prevention
    - 데드락의 발생 조건 중 하나를 방지하여 데드락을 미연에 방지하는 방법
        1. Mutual Exclusion : 공유할 수 없는 자원(CPU 등)은 동시 접근을 허용할 수 없어 불가능하다.
        2. Hold and Wait : 프로세스가 자원을 요청할 때 다른 어떤 자원도 가지고 있지 않아야 한다.
            1. 프로세스 시작 시 모든 필요한 자원을 할당받거나
            2. 자원이 필요할 때는 보유한 자원을 모두 포기하고 다시 요청
        3. No Preemtion
            1. process가 어떤 자원을 기다려야 하는 경우 이미 보유한 자원이 선점됨
            2. 모든 필요한 자원을 얻을 수 있을 때 그 프로세스는 다시 시작된다.
            3. 상태를 쉽게 저장하고 복원할 수 있는 자원에서 주로 사용된다. (CPU, memory)
        4. Circular Wait
            1. 모든 자원 유형에 할당 순서를 정하여 정해진 순서대로만 자원을 할당한다.
    
    ⇒ Utilization 저하, throughput 감소, starvation 문제
    
- Deadlock Avoidance
    - 자원 요청에 대한 부가정보를 이용해서 자원 할당이 deadlock으로부터 안전한지를 동적으로 조사해서 안전한 경우에만 할당
    - 가장 단순한 방법은 프로세스로 하여금 필요한 자원의 최대 사용량을 미리 선언하도록 하는 방법
    - Banker's Algorithm
        - 여러 개의 프로세스와 자원이 여러 개일 때 자원을 할당해도 되는 지 판별하는 알고리즘
        - 각 프로세스의 최대 사용량과 가용 자원을 비교하여 최대 사용량을 모두 제공할 수 있는 경우에만 자원을 할당해준다.

- Deadlock Detection and recovery
    - Deadlock 발생은 허용하되 그에 대한 detection 루틴을 두어 deadlock 발견시 recover

- Deadlock Ignorance
    - Deadlock을 시스템이 책임지지 않음
    - 대부분의 OS가 이 방법을 택함
