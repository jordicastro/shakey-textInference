#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

struct Robot {
    ll P, M;
};

// Function to check if we can achieve at least 'target' production rate within budget M
bool canAchieveRate(vector<Robot>& robots, ll target, ll budget) {
    ll cost = 0;
    for (auto& robot : robots) {
        if (robot.P < target) {
            cost += (target - robot.P) * robot.M;
            if (cost > budget) return false; // If cost exceeds budget, return false early
        }
    }
    return cost <= budget;
}

ll maxProduction(vector<Robot>& robots, ll budget) {
    ll lo = 0, hi = 1e12, best = 0;
    while (lo <= hi) {
        ll mid = lo + (hi - lo) / 2;
        if (canAchieveRate(robots, mid, budget)) {
            best = mid; // Save the maximum achievable production rate
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        ll M;
        cin >> N >> M;

        vector<Robot> robots(N);
        for (int i = 0; i < N; i++) {
            cin >> robots[i].P >> robots[i].M;
        }

        // Find the maximum production rate we can achieve within budget M
        cout << maxProduction(robots, M) << "\n";
    }
    return 0;
}
