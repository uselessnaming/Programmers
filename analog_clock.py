# 아날로그 시계
# 2024.06.09
# 해설 참조했음
def solution(h1, m1, s1, h2, m2, s2):
    cnt = 0

    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2

    # 0 혹은 12로 시작할 때 Counting이 되지 않는 것을 방지
    if start_time == 0 or start_time == 12 * 3600:
        cnt += 1

    while start_time < end_time:
        h_current_angle = start_time / 120 % 360
        m_current_angle = start_time / 10 % 360
        s_current_angle = start_time * 6 % 360

        h_next_angle = 360 if (start_time + 1) / 120 % 360 == 0 else (start_time + 1) / 120 % 360
        m_next_angle = 360 if (start_time + 1) / 10 % 360 == 0 else (start_time + 1) / 10 % 360
        s_next_angle = 360 if (start_time + 1) * 6 % 360 == 0 else (start_time + 1) * 6 % 360

        if s_current_angle < h_current_angle and s_next_angle >= h_next_angle:
            cnt += 1
        if s_current_angle < m_current_angle and s_next_angle >= m_next_angle:
            cnt += 1
        if s_next_angle == m_next_angle and s_next_angle == h_next_angle:
            cnt -= 1
        start_time += 1

    return cnt

h1 = 0
m1 = 5
s1 = 30
h2 = 0
m2 = 7
s2 = 0
# result 2

h11 = 12
m11 = 0
s11 = 0
h21 = 12
m21 = 0
s21 = 30
# result 1

h12 = 0
m12 = 6
s12 = 1
h22 = 0
m22 = 6
s22 = 6
# result 0

h13 = 11
m13 = 59
s13 = 30
h23 = 12
m23 = 0
s23 = 0
# result 1

h14 = 1
m14 = 5
s14 = 5
h24 = 1
m24 = 5
s24 = 6
# result 2

h15 = 0
m15 = 0
s15 = 0
h25 = 23
m25 = 59
s25 = 59
# result 2852

print(solution(h15, m15, s15, h25, m25, s25))