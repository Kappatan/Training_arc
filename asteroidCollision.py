def asteroidCollision( asteroids: List[int]) :
    st=[asteroids[0]]
    for i in range(1,len(asteroids)):
        if asteroids[i]>0:
            st.append(asteroids[i])
        else:
            k=asteroids[i]
            while d<0:
                d=asteroids[i]
                k=st.pop()
                if k>abs(asteroids[i]):
                    st.append(k)
                    d=k
                elif k<abs(asteroids[i]):
                    st.append(asteroids[i])


    return st