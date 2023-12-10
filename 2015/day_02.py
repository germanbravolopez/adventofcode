f = open('inputs/day_02_input.txt', 'r').read().strip().split('\n')
total_area_wp, total_dist_bow = 0, 0
for present in f:
    l, w, h = map(int, present.split('x'))
    total_area_wp += 2*l*w + 2*w*h + 2*h*l + sorted([l, w, h])[:2][0]*sorted([l, w, h])[:2][1]
    total_dist_bow += 2 * sorted([l, w, h])[:2][0] + 2 * sorted([l, w, h])[:2][1] + l*w*h
print(total_area_wp)
print(total_dist_bow)
