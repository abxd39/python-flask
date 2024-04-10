import json
import random

import flask
import time

app = flask.Flask(__name__)


@app.route('/api/v1/portal/video_seg', methods=['POST'])
def seg():
    # print(dir(flask.request))
    # print(flask.request.headers)
    # print(flask.request.data, flask.request.json, flask.request.args)
    print(flask.request.form)
    print(flask.request.files)
    time.sleep(30)
    return flask.jsonify({
        "ret_code": "0",
        "message": "",
        "data": {
            "scene_in_seconds": [{'scene_list': [0, 24.916]}, {'scene_list': [24.916, 36.65]},
                                 {'scene_list': [36.65, 77.916]}, {'scene_list': [77.916, 135.182]},
                                 {'scene_list': [135.182, 277.91]}],
            "cos_urls": [
                'https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/arthub/2021-10-28 17-47-31.mp4',
                'https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/arthub/2021-10-29 18-06-18.mp4',
                'https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_pubgm/google_drive/RG02387-PUBGM-V-1-FR-TENCENT.mp4',
                'https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/arthub/2021-10-28 20-04-13.mp4'
            ],
            "raw_file": "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/arthub/2021-10-28 17-47-31.mp4"
        }
    })


@app.route('/api/v1/portal/video_cover', methods=['POST'])
def cover():
    print(flask.request.form)
    print(flask.request.files)
    time.sleep(20)
    return flask.jsonify({
        'ret_code': '0',
        'message': '',
        'data': {
            'key_frame_at': 24.12,
            'cover_cos_url': 'https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0024_0.jpg',
            "raw_file": "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/arthub/2021-10-28 17-47-31.mp4"
        }
    })


@app.route('/api/v1/portal/video_tagging', methods=['POST'])
def tag():
    print(flask.request.form)
    print(flask.request.files)
    time.sleep(30)
    return flask.jsonify({
        'ret_code': '0',
        'message': '',
        'data': {
            'scene_in_seconds': [{'scene_list': [0, 24.916]}, {'scene_list': [24.916, 36.65]},
                                 {'scene_list': [36.65, 77.916]}, {'scene_list': [77.916, 135.182]},
                                 {'scene_list': [135.182, 277.91]}],
            'key_frames_url': [
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0024_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0036_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0076_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0133_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0273_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0280_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0319_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0326_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0328_0.jpg",
                "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/thumbnail/110347130677152/0364_0.jpg"
            ],
            'tags': ['3D_first_person', '3D_third_person', 'display', 'game_engine_generated_n_screen_recording',
                     'has_text', 'music_slow', 'sound_effect_only'],
            "raw_file": "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/cvinsights_avtr/arthub/2021-10-28 17-47-31.mp4"
        }
    })


@app.route('/api/v1/portal/add_user', methods=['POST'])
def add_user():
    print(flask.request.json)
    return flask.jsonify({
        'ret_code': '0',
        'message': 'add success',
        'data': {}
    })


@app.route('/api/v1/portal/update_user', methods=['POST'])
def update_user():
    print(flask.request.json)
    return flask.jsonify({
        'ret_code': '0',
        'message': 'update success',
        'data': {}
    })


@app.route('/api/v1/portal/del_user', methods=['POST'])
def del_user():
    print(flask.request.json)
    return flask.jsonify({
        'ret_code': '0',
        'message': 'del success',
        'data': {}
    })


@app.route('/api/v1/portal/search_user', methods=['POST'])
def search_user():
    print(flask.request.json)
    fuzzy = flask.request.json.get('fuzzy')
    if fuzzy == 1:
        return flask.jsonify({
            'ret_code': '0',
            'message': 'add success',
            'data': [
                {
                    "username": "lilysun",
                    "cn_name": "",
                    "role_id": 1,
                    "create_time": '2022-10-12 15:55:55',
                    "update_time": '2022-10-12 15:55:55'
                }
            ]
        })
    data_list = []
    for i in range(25):
        role_id = random.randint(1, 3)
        data_list.append(
            {
                "username": "gc_suzhipeng",
                "cn_name": "苏志鹏",
                "role_id": role_id,
                "create_time": '2022-10-12 15:55:55',
                "update_time": '2022-10-12 15:55:55'
            }
        )
    pagenum = flask.request.json['pagenum']
    pagesize = flask.request.json['pagesize']
    new_data = data_list[pagesize * (pagenum - 1): pagesize * pagenum]
    return flask.jsonify({
        'ret_code': '0',
        'message': 'add success',
        'total': len(data_list),
        'data': new_data
    })


@app.route('/api/v1/portal/summary', methods=['GET'])
def summary():
    print(flask.request.json)
    return flask.jsonify({
        "comment2topic": [
            {
                "content": "Major lag issue with great ping",
                "tier3_topic": "high ping, high latency"
            },
            {
                "content": "There is a delay on the ping display when your ping get high.  You will have these input delays at high ping (150 and above).  It could be an issue with your connection being unstable which will at times give you great ping and others cause you to run into turrets and not cast skills or level up correctly.  I've been there many times, do not try to play like this.  It also could be the server.  You shouldn't have an issue if youre playing solo but teaming up with friends can pull you into different regions, so even with good internet, if youre playing on a server in Japan from Spain, it will always have this lag.  Be careful whom you match up with because that may be the issue. Things you can do to help:  Settings:  outline off, screen shake off, hd mode off, shadow off, refresh rate high, graphics smooth  &amp;#x200B;  &amp;#x200B;  That should make the gme a smooth as possible for you. Hope this helps",
                "tier3_topic": "high ping, high latency"
            },
            {
                "content": "Obviously not. I’m talking when my ping is 50ms and below. This example, it was upper 200s. My point is, it does this with 50ms and below, and 200ms and above. Doesn’t seem to matter, so I don’t think the ping is the issue here.",
                "tier3_topic": "high ping"
            },
            {
                "content": "Are u playing on samsung s22 ultra? This mobile phone has the baddest ping stabilisation  to play ml.",
                "tier3_topic": "high ping"
            }
        ],
        "comments": [
            {
                "comment_uin": "70b399318ac8ef8b0cea5544ea0291ff",
                "content": "Major lag issue with great ping"
            },
            {
                "comment_uin": "cf80bf9e328520a7e806c49e2d2e0b03",
                "content": "There is a delay on the ping display when your ping get high.  You will have these input delays at high ping (150 and above).  It could be an issue with your connection being unstable which will at times give you great ping and others cause you to run into turrets and not cast skills or level up correctly.  I've been there many times, do not try to play like this.  It also could be the server.  You shouldn't have an issue if youre playing solo but teaming up with friends can pull you into different regions, so even with good internet, if youre playing on a server in Japan from Spain, it will always have this lag.  Be careful whom you match up with because that may be the issue. Things you can do to help:  Settings:  outline off, screen shake off, hd mode off, shadow off, refresh rate high, graphics smooth  &amp;#x200B;  &amp;#x200B;  That should make the gme a smooth as possible for you. Hope this helps"
            },
            {
                "comment_uin": "1b8bd3424ce753ecdbf4c9f636494805",
                "content": "Obviously not. I’m talking when my ping is 50ms and below. This example, it was upper 200s. My point is, it does this with 50ms and below, and 200ms and above. Doesn’t seem to matter, so I don’t think the ping is the issue here."
            },
            {
                "comment_uin": "b277b9c500bef21250baf739486f0696",
                "content": "Are u playing on samsung s22 ultra? This mobile phone has the baddest ping stabilisation  to play ml."
            }
        ],
        "data_detail": {
            "end_time": "2022-10-19 00:00:00",
            "game_name": "MLBB",
            "start_time": "2022-10-18 00:00:00"
        },
        "status_code": 200,
        "tier2_topic": "lag",
        "tier3_topic": [
            "high latency",
            "high ping",
            "network connection",
            "frame drop",
            "others"
        ],
        "timestamps": {
            "data_obtain": "0:00:00",
            "summary": "0:00:00",
            "tier3_classification": "0:00:00"
        },
        "topic2summary": {
            "high latency": "Major lag issue with great ping.\nYou will have these input delays at high ping (150 and above).\nIt could be an issue with your connection being unstable which will at times give you great ping and others cause you to run into turrets and not cast skills or level up correctly.",
            "high ping": "Major lag issue with great ping.\nYou will have these input delays at high ping (150 and above).\nIt could be an issue with your connection being unstable which will at times give you great ping and others cause you to run into turrets and not cast skills or level up correctly."
        },
        "type": "SUCCESS"
    })


@app.route('/api/v1/portal/new_install_quarter', methods=['GET'])
def new_quarter():
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": [
            "2022-Q3",
            "2022-Q2",
            "2022-Q1"
        ]
    })


@app.route('/api/v1/portal/new_install_report', methods=['POST'])
def new_install_report():
    # time.sleep(1.5)
    print(flask.request.json)
    return flask.jsonify({"ret_code": "0", "message": "0",
                          "data": {"spend_total": {"algo": 4695419.68, "others": 5443263.19},
                                   "spend": [{"game_code": "幻塔", "algo": 55, "others": 496708, "rate": 0.01},
                                             {"game_code": "AOV-IN", "algo": 0, "others": 0, "rate": "NaN"},
                                             {"game_code": "AOV-INTL", "algo": 0, "others": 34366, "rate": 0},
                                             {"game_code": "AOV-JP", "algo": 0, "others": 7821, "rate": 0},
                                             {"game_code": "Fashion Dream", "algo": 381.68,
                                              "others": 538758.19, "rate": 0.07},
                                             {"game_code": "HOK-INTL", "algo": 258252, "others": 228104, "rate": 53.1},
                                             {"game_code": "PUBG Mobile", "algo": 4264863, "others": 2571870,
                                              "rate": 62.38},
                                             {"game_code": "妄想山海-INTL", "algo": 171868, "others": 1565636,
                                              "rate": 9.89}],
                                   "retention_cpr": [
                                       {"game_code": "幻塔", "d2_algo": 54.81, "d2_others": 23.04, "d2_rate": 138,
                                        "d7_algo": 0, "d7_others": 64.38, "d7_rate":-100},
                                       {"game_code": "AOV-IN", "d2_algo": 0, "d2_others": 0, "d2_rate": 0, "d7_algo": 0,
                                        "d7_others": 0, "d7_rate": 0},
                                       {"game_code": "AOV-INTL", "d2_algo": 0, "d2_others": 0, "d2_rate": 0,
                                        "d7_algo": 0,
                                        "d7_others": 0, "d7_rate": 0},
                                       {"game_code": "AOV-JP", "d2_algo": 0, "d2_others": 0, "d2_rate": 0, "d7_algo": 0,
                                        "d7_others": 0, "d7_rate": 0},
                                       {"game_code": "Fashion Dream", "d2_algo": 0, "d2_others": 0, "d2_rate": 0,
                                        "d7_algo": 0, "d7_others": 0, "d7_rate": 0},
                                       {"game_code": "HOK-INTL", "d2_algo": 1.69,
                                        "d2_others": 4.01, "d2_rate":-57.99, "d7_algo": 0,
                                        "d7_others": 0, "d7_rate": 0},
                                       {"game_code": "PUBG Mobile", "d2_algo": 0.57,
                                        "d2_others": 0.82, "d2_rate":-30, "d7_algo": 2.30,
                                        "d7_others": 2.92, "d7_rate":-21},
                                       {"game_code": "妄想山海-INTL", "d2_algo": 0, "d2_others": 0, "d2_rate": 0,
                                        "d7_algo": 0,
                                        "d7_others": 0, "d7_rate": 0}], "retention_roi": [
                                  {"game_code": "幻塔", "d2_algo": 0.02, "d2_others": 0.04, "d2_rate":-50, "d7_algo": 0,
                                   "d7_others": 0.02, "d7_rate":-1},
                                  {"game_code": "AOV-IN", "d2_algo": 94, "d2_others": 54, "d2_rate": 74, "d7_algo": 0,
                                   "d7_others": 0, "d7_rate": 0},
                                  {"game_code": "AOV-INTL", "d2_algo": 609, "d2_others": 318, "d2_rate": 92,
                                   "d7_algo": 0, "d7_others": 0, "d7_rate": 0},
                                  {"game_code": "AOV-JP", "d2_algo": 1, "d2_others": 1, "d2_rate": 0, "d7_algo": 0,
                                   "d7_others": 0, "d7_rate": 0},
                                  {"game_code": "Fashion Dream", "d2_algo": 2, "d2_others": 261, "d2_rate":-99,
                                   "d7_algo": 0, "d7_others": 0, "d7_rate": 0},
                                  {"game_code": "HOK-INTL", "d2_algo": 0.59, "d2_others": 0.25,
                                   "d2_rate": 136, "d7_algo": 0, "d7_others": 0, "d7_rate": 0},
                                  {"game_code": "PUBG Mobile", "d2_algo": 1.75, "d2_others": 1.22,
                                   "d2_rate": 43, "d7_algo": 0.43, "d7_others": 0.34,
                                   "d7_rate": 0.26},
                                  {"game_code": "妄想山海-INTL", "d2_algo": 15, "d2_others": 22, "d2_rate":-32,
                                   "d7_algo": 0, "d7_others": 0, "d7_rate": 0}]}})


@app.route('/api/v1/portal/nlp_report', methods=['POST'])
def nlp_report():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": [
            {
                "date": "2022-10-24",
                "opinion_pv": 100,
                "opinion_uv": 50,
                "intelligence_pv": 100,
                "intelligence_uv": 50,
                "databrain_pv": 1000,
                "databrain_uv": 500,
                "opinion_pv_rate": 0.2,
                "opinion_uv_rate": 0.3,
                "intelligence_pv_rate": 0.4,
                "intelligence_uv_rate": 0.11
            },
            {
                "date": "2022-10-18",
                "opinion_pv": 100,
                "opinion_uv": 50,
                "intelligence_pv": 100,
                "intelligence_uv": 50,
                "databrain_pv": 1000,
                "databrain_uv": 500,
                "opinion_pv_rate": 0.2,
                "opinion_uv_rate": 0.3,
                "intelligence_pv_rate": 0.4,
                "intelligence_uv_rate": 0.11
            }
        ]
    }
    )


@app.route('/api/v1/portal/service_report', methods=['POST'])
def service_report():
    print(flask.request.json)
    # time.sleep(1)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":
            [
                {
                    "service_name": "base-en-keyword-extraction1",
                    "avg_qps": 0,
                    "max_qps": 4000,
                    "err_rate": 0.05,
                    "avg_latency": 200,
                    "cpu_usage_rate": 0.7,
                    "cpu_request": 11,
                    "memory_usage_rate": 50,
                    "memory_request": 11,
                    "cost": 14111,
                    "date": '2023-08-29',
                    "max_cpu_usage": 50,
                    "max_mem_usage": 11,
                    "gpu_usage": 12,
                    "max_gpu_usage": 18,
                    "gpu_request": 22
                },
                {
                    "service_name": "service-01",
                    "avg_qps": 0.1234564,
                    "max_qps": 0,
                    "err_rate": 0.05,
                    "avg_latency": 200,
                    "cpu_usage_rate": 0,
                    "cpu_request": 11,
                    "memory_usage_rate": 0.11,
                    "memory_request": 11,
                    "cost": 141.001156,
                    "date": '2023-08-30',
                    "max_cpu_usage": 0,
                    "max_mem_usage": 0,
                    "gpu_usage": 12,
                    "max_gpu_usage": 18,
                    "gpu_request": 22
                },
                {
                    "service_name": "service-02",
                    "avg_qps": 200,
                    "max_qps": 4000,
                    "err_rate": 0.05,
                    "avg_latency": 200,
                    "cpu_usage_rate": 0.7,
                    "cpu_request": 11,
                    "memory_usage_rate": 25,
                    "memory_request": 11,
                    "cost": 141,
                    "date": '2023-08-27',
                    "max_cpu_usage": 50,
                    "max_mem_usage": 11,
                    "gpu_usage": 12,
                    "max_gpu_usage": 18,
                    "gpu_request": 22
                },
                {
                    "service_name": "base-en-keyword-extraction2",
                    "avg_qps": 1000,
                    "max_qps": 4000,
                    "err_rate": 0.05,
                    "avg_latency": 200,
                    "cpu_usage_rate": 0.7,
                    "cpu_request": 11,
                    "memory_usage_rate": 0.11,
                    "memory_request": 11,
                    "cost": 18.12541,
                    "date": '2022-10-20',
                    "max_cpu_usage": 50,
                    "max_mem_usage": 11,
                    "gpu_usage": 12,
                    "max_gpu_usage": 18,
                    "gpu_request": 22
                }
            ]
    }
    )


@app.route('/api/v1/portal/cv_report', methods=['POST'])
def cv_report():
    # time.sleep(1.5)
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":
            [
                {
                    "date": "2022-10-01",
                    "new_add": 30,
                    "sum": 900,
                    "success_rate": 60
                },
                {
                    "date": "2022-10-02",
                    "new_add": 200,
                    "sum": 1000,
                    "success_rate": 70
                },
                {
                    "date": "2022-10-01",
                    "new_add": 300,
                    "sum": 1100,
                    "success_rate": 98
                }
            ]
    })


@app.route('/api/v1/portal/login', methods=['GET'])
def login():
    print(flask.request.json)
    return flask.redirect(
        'https://login.iam.intlgame.com/sso/tn-869bbe512bb54c14921d85c69ae839dc/ai-72979cb3b5224f4f9a19ca6b4e2fe64c/oidc/authorize?client_id=ai-72979cb3b5224f4f9a19ca6b4e2fe64c&response_type=code&redirect_uri=http://algo.intltest11.com/&scope=openid offline_access')


def callData():
    return {
        "ret_code": "0",
        "message": "success",
        "data": {
            "user_name": "gc_suzhipeng"
        }
    }


@app.route('/api/v1/portal/callback', methods=['GET'])
def callback():
    resp = flask.make_response()
    resp.set_cookie('user_name', 'gc_suzhipeng')
    resp.set_cookie('code', '123456')
    # resp.set_cookie('user_name', 'gc_suzhipeng', max_age=24 * 60 * 60)
    return resp


@app.route('/api/v1/portal/portal_report', methods=['POST'])
def portal_report():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success"
    })


@app.route('/api/v1/portal/interface_test', methods=['POST'])
def interface_test():
    print(flask.request.json)
    j_str = json.dumps({
        "ret_code": "0",
        "message": "success",
        "data": {
            "name": "tom"
        }
    })
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": {
            "result": j_str,
            "time": 3000
        }
    })


@app.route('/api/v1/portal/stress_test', methods=['POST'])
def stress_test():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": {
            "db_id": 1
        }
    })


@app.route('/api/v1/portal/stress_report', methods=['POST'])
def stress_report():
    print(flask.request.json)
    db_id = flask.request.json.get('db_id')
    if db_id:
        return flask.jsonify({
            "ret_code": "0",
            "message": "success",
            "data": [
                {
                    "raw_info": {
                        "user_name": "gc_suzhipeng",
                        "service_name": "ug-algo-portal-dev222",
                        "url": "http://43.134.152.100:8080/api/v1/portal/service_report",
                        "protocol": "POST",
                        "headers": [
                            {
                                "key": "Content-Type",
                                "value": "application/json"
                            },
                            {
                                "key": "Connection",
                                "value": "keep-alive"
                            }
                        ],
                        "body": [
                            '{"name": "tom"}',
                            '{"age": 18}'
                        ],
                        "con_num": 3,
                        "duration_time": 10,
                        "create_time": "2022-11-16 15:30:30",
                        "db_id": db_id,
                        "status": 3
                    },
                    "stress_result": {
                        "success_rate": 80,
                        "avg_latency": 580,
                        "max_latency": 1080,
                        "min_latency": 180,
                        "qps": 100,
                        "p95": 30.1,
                        "p99": 35.25,
                        "err_info": [
                            "Welcome to our algorithm portal, which provides access to our team's Polaris metrices, a large number of algorithm service demos, and a variety of tools to improve productivity",
                            "Welcome to our algorithm portal, which provides access to our team's Polaris metrices, a large number of algorithm service demos, and a variety of tools to improve productivity",
                            "Welcome to our algorithm portal, which provides access to our team's Polaris metrices, a large number of algorithm service demos, and a variety of tools to improve productivity"
                        ]
                    }
                }
            ]
        })
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "total": 4,
        "data": [
            {
                "raw_info": {
                    "user_name": "gc_suzhipeng",
                    "service_name": "ug-algo-portal-dev222",
                    "url": "http://43.134.152.100:8080/api/v1/portal/service_report",
                    "protocol": "POST",
                    "headers": [
                        # {
                        #     "key": "Content-Type",
                        #     "value": "application/json"
                        # },
                        # {
                        #     "key": "Connection",
                        #     "value": "keep-alive"
                        # }
                    ],
                    "body": [
                        # '{"name": "Jack", "age": 20}'
                    ],
                    "con_num": 3,
                    "duration_time": 1,
                    "create_time": "2022-11-16 15:30:30",
                    "db_id": 4,
                    "status": 1
                },
                "stress_result": {
                    "success_rate": 80,
                    "avg_latency": 580,
                    "max_latency": 1080,
                    "min_latency": 180,
                    "qps": 100,
                    "p95": 30.1,
                    "p99": 35.25,
                    "err_info": [
                    ]
                }
            },
            {
                "raw_info": {
                    "user_name": "gc_suzhipeng",
                    "service_name": "ug-algo-portal-dev111",
                    "url": "http://43.134.152.100:8080/api/v1/portal/service_report",
                    "protocol": "POST",
                    "headers": [
                        {
                            "key": "Content-Type",
                            "value": "application/json"
                        },
                        {
                            "key": "Connection",
                            "value": "keep-alive"
                        }
                    ],
                    "body": [
                        '{"name": "tom"}',
                        '{"age": 18}'
                    ],
                    "con_num": 3,
                    "duration_time": 100,
                    "create_time": "2022-11-14 15:30:30",
                    "db_id": 3,
                    "status": 2
                },
                "stress_result": {
                    "success_rate": 80,
                    "avg_latency": 580,
                    "max_latency": 1080,
                    "min_latency": 180,
                    "qps": 100,
                    "p95": 30.1,
                    "p99": 35.25,
                    "err_info": [
                        "Welcome to our algorithm portal, which provides access to our team's Polaris metrices, a large number of algorithm service demos, and a variety of tools to improve productivity",
                        "Welcome to our algorithm portal, which provides access to our team's Polaris metrices, a large number of algorithm service demos, and a variety of tools to improve productivity",
                        "Welcome to our algorithm portal, which provides access to our team's Polaris metrices, a large number of algorithm service demos, and a variety of tools to improve productivity"
                    ]
                }
            },
            {
                "raw_info": {
                    "user_name": "gc_suzhipeng",
                    "service_name": "ug-algo-portal-dev111",
                    "url": "http://43.134.152.100:8080/api/v1/portal/service_report",
                    "protocol": "POST",
                    "headers": [
                        {
                            "key": "Content-Type",
                            "value": "application/json"
                        },
                        {
                            "key": "Connection",
                            "value": "keep-alive"
                        }
                    ],
                    "body": [
                        '{"name": "tom"}',
                        '{"age": 18}'
                    ],
                    "con_num": 3,
                    "duration_time": 100,
                    "create_time": "2022-11-14 15:30:30",
                    "db_id": 2,
                    "status": 3
                },
                "stress_result": {
                    "success_rate": 80,
                    "avg_latency": 580,
                    "max_latency": 1080,
                    "min_latency": 180,
                    "qps": 100,
                    "p95": 0,
                    "p99": 0,
                    "err_info": [
                        "net error",
                        "time out"
                    ]
                }
            },
            {
                "raw_info": {
                    "user_name": "gc_suzhipeng",
                    "service_name": "ug-algo-portal-dev111",
                    "url": "http://43.134.152.100:8080/api/v1/portal/service_report",
                    "protocol": "POST",
                    "headers": [
                        {
                            "key": "Content-Type",
                            "value": "application/json"
                        },
                        {
                            "key": "Connection",
                            "value": "keep-alive"
                        }
                    ],
                    "body": [
                        '{"name": "tom"}',
                        '{"age": 18}'
                    ],
                    "con_num": 3,
                    "duration_time": 100,
                    "create_time": "2022-11-14 15:30:30",
                    "db_id": 1,
                    "status": 4
                },
                "stress_result": {
                    "success_rate": 80,
                    "avg_latency": 580,
                    "max_latency": 1080,
                    "min_latency": 180,
                    "qps": 100,
                    "p95": 30.1,
                    "p99": 35.25,
                    "err_info": [
                        "net error",
                        "time out"
                    ]
                }
            }
        ]
    })


@app.route('/api/v1/portal/terminate_stress_test', methods=['POST'])
def terminate_stress_test():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success"
    })


@app.route('/api/v1/portal/get_portal_report', methods=['POST'])
def get_portal_report():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": {
            "total_data": [
                {
                    "date": "2022-11-03",
                    "pv": 100,
                    "uv": 20
                },
                {
                    "date": "2022-11-04",
                    "pv": 150,
                    "uv": 15
                },
                {
                    "date": "2022-11-05",
                    "pv": 200,
                    "uv": 10
                },
                {
                    "date": "2022-11-06",
                    "pv": 50,
                    "uv": 5
                },
                {
                    "date": "2022-11-07",
                    "pv": 200,
                    "uv": 8
                },
                {
                    "date": "2022-11-08",
                    "pv": 20,
                    "uv": 2
                },
                {
                    "date": "2022-11-09",
                    "pv": 40,
                    "uv": 2
                }
            ],
            "table_data":
                [
                    {
                        "page_name": "Audience For New Report",
                        "pv": 1000,
                        "uv": 30,
                        "pv_percentage": 20
                    },
                    {
                        "page_name": "Aspect Based Sentiment Analysis",
                        "pv": 100,
                        "uv": 20,
                        "pv_percentage": 20
                    },
                    {
                        "page_name": "Public Opinion Topic Identification",
                        "pv": 100,
                        "uv": 20,
                        "pv_percentage": 20
                    },
                    {
                        "page_name": "Public Opinion Topic Identification",
                        "pv": 100,
                        "uv": 20,
                        "pv_percentage": 20
                    },
                    {
                        "page_name": "Public Opinion Topic Identification",
                        "pv": 100,
                        "uv": 20,
                        "pv_percentage": 20
                    },
                    {
                        "page_name": "Public Opinion Topic Identification",
                        "pv": 100,
                        "uv": 20,
                        "pv_percentage": 20
                    },
                    {
                        "page_name": "Audience For New Report",
                        "pv": 100,
                        "uv": 20,
                        "pv_percentage": 20
                    },
                    {
                        "page_name": "Audience For New Report",
                        "pv": 100,
                        "uv": 20,
                        "pv_percentage": 20
                    }
                ]
        }
    })


@app.route('/api/v1/portal/churning_quarter', methods=['GET'])
def churning_quarter():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": [
            "2022-Q4",
            "2022-Q3",
            "2022-Q2"
        ]
    })


@app.route('/api/v1/portal/churning_report', methods=['POST'])
def churning_report():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":
            [
                {
                    "game_code": "pubgm",
                    "spend": 10000,
                    "cohort_size": 100000,
                    "spend_by_cohort": 0.1,
                    "d1_retention": 53.16,
                    "d7_retention": 19.40,
                },
                {
                    "game_code": "AOV-INTL",
                    "spend": 10000,
                    "cohort_size": 100000,
                    "spend_by_cohort": 0.1,
                    "d1_retention": 53.16,
                    "d7_retention": 19.40,
                }
            ]
    })


@app.route('/api/v1/portal/pre_churning_report', methods=['POST'])
def pre_churning_report():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":
            [
                {
                    "game_code": "pubgm",
                    "active_time_uplift": 50.0,
                    "login_times_uplift": 61.9,
                    "arpu_uplift": 28.9,
                    "d1_retention": 26.1,
                    "d7_retention": 46.0,
                },
                {
                    "game_code": "AOV-INTL",
                    "active_time_uplift": 50.0,
                    "login_times_uplift": 61.9,
                    "arpu_uplift": 28.9,
                    "d1_retention": 26.1,
                    "d7_retention": 46.0,
                }
            ]
    })


@app.route('/api/v1/portal/automation_quarter', methods=['GET'])
def automation_quarter():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": [
            "2022-Q4",
            "2022-Q3",
            "2022-Q2"
        ]
    })


@app.route('/api/v1/portal/automation_report', methods=['POST'])
def automation_report():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":
            [
                {
                    "category": "Trust",
                    "game_code": "pubgm",
                    "country": "BR",
                    "spend": 10000,
                    "kpi": "D1 Register Rate",
                    "improvement": 11.68
                },
                {
                    "category": "Trust",
                    "game_code": "pubgm",
                    "country": "BR",
                    "spend": 10000,
                    "kpi": "D1 Register Rate",
                    "improvement": 11.68
                }
            ]
    })


@app.route('/aidraw/api/batch_draw', methods=['POST'])
def batchdraw():
    # print(flask.request.json)
    # time.sleep(1)
    return flask.jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "task_id": 17,
            "creator": "gc_suzhipeng",
            "caption_num": 2,
            "total_img_num": 2,
            "create_time": "2023-02-07 10:00:00"
        }
    })

# @app.route('/predict', methods=['POST'])
# def predict():
#     print(flask.request.json)
#     time.sleep(1)
#     return flask.jsonify({
#         "ret_code": "0",
#         "message": "successful",
#         "data": {
#             "pred_label": 0,
#             "pred_score": 0.944,
#             "task_id": 1
#         },
#         "session_data": {}
#     })

# @app.route('/predict/', methods=['POST'])
# def text_extract():
#     print(flask.request.json)
#     time.sleep(1)
#     return flask.jsonify({
#         "data": {
#             "keywords": [
#                 [
#                     "good game",
#                     "not recommend"
#                 ]
#             ],
#             "trans_languages": [
#                 "en",
#                 "zh",
#                 "pt",
#                 "zh-tw",
#                 "es"
#             ]
#         },
#         "message": "success",
#         "ret_code": "0",
#         "session_data": {}
#     })

# @app.route('/predict/', methods=['POST'])
# def comment_analysis():
#     print(flask.request.json)
#     time.sleep(1)
#     return flask.jsonify({
#         "data": [
#             {
#                 "content": "Lian Po é igual o Ormar do AoV,chato pra porra kkkk,ainda bem que não tão jogando com ele de Sup ainda",
#                 "key": "md5_1",
#                 "label": "high",
#                 "score": {
#                     "high": 0.981,
#                     "low": 0.002,
#                     "medium": 0.017
#                 }
#             }
#         ],
#         "message": "success",
#         "ret_code": "0",
#         "session_data": {}
#     })


@app.route('/api/v1/portal/automation/campaign', methods=['POST'])
def campaign():
    print(flask.request.json)
    if 'campaign_name' in flask.request.json:
        return flask.jsonify({
            "ret_code": "0",
            "message": "0",
            "data": [
                {
                    "name": "Google-DE-AND-191219-UAC2.5-purchase-lanhan-sdk-newinstall-WEU",
                    "budget": 200
                }
            ]
        })
    return flask.jsonify({
        "ret_code": "0",
        "message": "0",
        "data": [
            {"name": "Google-EU-AND-230515-UAC3.0_PLTV-EU-newinstall-EU", "budget": 2000},
            {"name": "Google-JP-AND-230129-install-AC3.0-newinstall-JP", "budget": 12000},
            {"name": "Google-JP-AND-230517-AC2.5-pre&similar-newinstall-JP", "budget": 2000},
            {"name": "google-sea-AND-230427-UAC3.0-pltv_en_mayee-newinstall-SEA", "budget": 600}
        ]
    })


@app.route('/api/v1/portal/automation/rule_add', methods=['POST'])
def rule_add():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":
            {
                "rule_id": 123
            }
    })


@app.route('/api/v1/portal/automation/rule_query', methods=['POST'])
def rule_query():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":[
    {
        "rule_id":123,
        "game_code":"nikke",
        "rule_name":"test_rule",
        "creator":"gc_suzhipeng",
        "opt_level":"campaign",
        "create_time":"2023-03-06 04:13:00 +0000 UTC",
        "opt_target":{
            "openid":1,
            "metric":5
        },
        "opt_constraint":[
            {
                "key":"installs",
                "value":100,
                "scope":[
                    "Google-JP-AND-230129-install-AC3.0-newinstall-JP",
                    "Google-EU-AND-230515-UAC3.0_PLTV-EU-newinstall-EU"
                ]
            },
            {
                "key":"cpi",
                "value":0.5,
                "scope":[
                    "Google-EU-AND-230515-UAC3.0_PLTV-EU-newinstall-EU",
                    "Google-JP-AND-230129-install-AC3.0-newinstall-JP",
                    "Google-JP-AND-230517-AC2.5-pre&similar-newinstall-JP",
                    "google-sea-AND-230427-UAC3.0-pltv_en_mayee-newinstall-SEA"
                ]
            }
        ],
        "opt_objects":[
            "Google-EU-AND-230515-UAC3.0_PLTV-EU-newinstall-EU",
            "Google-JP-AND-230129-install-AC3.0-newinstall-JP",
            "Google-JP-AND-230517-AC2.5-pre&similar-newinstall-JP"
        ],
        "object_status":{
            "Google-EU-AND-230515-UAC3.0_PLTV-EU-newinstall-EU":"active",
            "Google-JP-AND-230129-install-AC3.0-newinstall-JP":"active",
            "Google-JP-AND-230517-AC2.5-pre&similar-newinstall-JP":"active"
        },
        "opt_budget":16000,
        "tracking_basis":1,
        "country":"Azerbaijan",
        "campaign_type":2,
        "start_date":"2023-6-10",
        "end_date":"2023-6-11",
        "subscribe":"unsubscribe"
    }
]
            
    })


@app.route('/api/v1/portal/automation/rule_update', methods=['POST'])
def rule_update():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success"
    })


@app.route('/api/v1/portal/automation/rule_del', methods=['POST'])
def rule_del():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success"
    })


@app.route('/api/v1/portal/automation/opt_calculate', methods=['POST'])
def opt_calculate():
    print(flask.request.json)
    time.sleep(1)
    if 'budget' in flask.request.json:
        return flask.jsonify({
            "ret_code": "0",
            "message": "success",
            "data": [
                {
                    "opt_budget": 700,
                    "solved": True,
                    "goal_improvement":0,
                    "total": {
                        "original": {
                            "budget": 700,
                            "media_budget":444,
                            "bid": 0,
                            "spend": 300,
                            "installs": 276.08978,
                            "cpi": 1.086603,
                            "registers": 230.20398,
                            "cohort_register_rate": 0.6232896,
                            "d1_cohort_register_rate": 0.4893754,
                            "d2_retention_rate": 0.50342476,
                            "d7_retention_rate": 0.10427435,
                            "cost_per_d2_retention": 2.5886304,
                            "cost_per_d7_retention": 12.497204,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                        },
                        "opt": {
                            "budget": 300,
                            "media_budget":111,
                            "bid": 0,
                            "spend": 300,
                            "installs": 276.0844,
                            "cpi": 1.0866241,
                            "registers": 230.20195,
                            "cohort_register_rate": 0.6232942,
                            "d1_cohort_register_rate": 0.4893787,
                            "d2_retention_rate": 0.5034261,
                            "d7_retention_rate": 0.1042747,
                            "cost_per_d2_retention": 2.588647,
                            "cost_per_d7_retention": 12.497272,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                        }
                    },
                    "details": [
                        {
                            "campaign_name": "Google-FR-AND-220520-UAC2.5-purchase-lanhan-sdk-newinstall-WEU",
                            "original": {
                                "budget": 700,
                                "media_budget":444,
                                "bid": 24.11,
                                "spend": 186.51027,
                                "installs": 184.16328,
                                "cpi": 1.0127441,
                                "registers": 147.86186,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5287864,
                                "cost_per_d7_retention": 12.246333,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                            },
                            "opt": {
                                "budget": 212,
                                "bid": 25.11,
                                "spend": 212,
                                "installs": 209.33226,
                                "cpi": 1.0127441,
                                "media_budget":111,
                                "registers": 168.06966,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5287905,
                                "cost_per_d7_retention": 12.246429,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                            }
                        },
                        {
                            "campaign_name": "Google-FR-AND-220524-UAC2.5-purchase_ggsa-lanhan-sdk-newinstall-WEU",
                            "original": {
                                "budget": 77.41936,
                                "bid": 24.11,
                                "spend": 77.41936,
                                "media_budget":444,
                                "installs": 58.72623,
                                "cpi": 1.3183095,
                                "registers": 54.661846,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.7450886,
                                "cost_per_d7_retention": 13.143728,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                            },
                            "opt": {
                                "budget": 88,
                                "bid": 24.11,
                                "spend": 88,
                                "media_budget":111,
                                "installs": 66.75215,
                                "cpi": 1.3183095,
                                "registers": 62.132298,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.7451003,
                                "cost_per_d7_retention": 13.143997,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                            }
                        }
                    ]
                }
            ]
        })
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "success",
            "data": [
                {
                    "opt_budget": 800,
                    "solved": True,
                    "goal_improvement":0.0459,
                    "total": {
                        "original": {
                            "budget": 800,
                            "media_budget":8888,
                            "bid": 10,
                            "spend":-800,
                            "installs": 536.23944,
                            "cpi": 1.086603,
                            "cpr": 1.0867368,
                            "registers": 613.8773,
                            "cohort_register_rate": 0.6232896,
                            "d1_cohort_register_rate": 0.4893754,
                            "d2_retention_rate": 0.50342476,
                            "d7_retention_rate": 0.10427435,
                            "cost_per_d2_retention": 2.5886445,
                            "cost_per_d7_retention": 12.497529,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d2_roas": 1,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                        },
                        "opt": {
                            "budget": 800,
                            "bid": 10,
                            "spend": 800,
                            "installs": 736.1488,
                            "cpi": 1.0867368,
                            "cpr": 1.0867368,
                            "registers": 613.84296,
                            "cohort_register_rate": 0.62331873,
                            "d1_cohort_register_rate": 0.4893962,
                            "d2_retention_rate": 0.50343287,
                            "d7_retention_rate": 0.10427658,
                            "cost_per_d2_retention": 2.5887477,
                            "cost_per_d7_retention": 12.49796,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d2_roas": 1,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                            "media_budget":111,
                        }
                    },
                    "details": [
                        {
                            "campaign_name": "Google-FR-AND-220520-UAC2.5-purchase-lanhan-sdk-newinstall-WEU",
                            "portrait": [],
                            "original": {
                                "budget": 1325.5132,
                                "bid": 24.11,
                                "spend":-1325.5132,
                                "installs": 1308.8334,
                                "cpi": 1.0127441,
                                "cpr": 1.0867368,
                                "registers": 1050.8422,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5288157,
                                "cost_per_d7_retention": 12.247024,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":444,
                            },
                            "opt": {
                                "budget": 565,
                                "bid": 24.11,
                                "spend": 565,
                                "installs": 557.8902,
                                "cpi": 1.0127441,
                                "cpr": 1.0867368,
                                "registers": 447.92148,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5288093,
                                "cost_per_d7_retention": 12.246872,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":111,
                            }
                        },
                        {
                            "campaign_name": "Google-FR-AND-220524-UAC2.5-purchase_ggsa-lanhan-sdk-newinstall-WEU",
                            "portrait": ["fresh", "cost_wave", "cpi_wave", "not_enough_spend", "compete"],
                            "original": {
                                "budget": 55190.31964,
                                "bid": 24.11,
                                "spend": 3055111.31964,
                                "installs": 418.20197,
                                "cpi": 1.3183095,
                                "cpr": 1.0867368,
                                "registers": 389.2586,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.7451723,
                                "cost_per_d7_retention": 13.145647,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":444,
                            },
                            "opt": {
                                "budget": 235,
                                "bid": 24.11,
                                "spend": 235,
                                "installs": 178.25858,
                                "cpi": 1.3183095,
                                "cpr": 1.0867368,
                                "registers": 165.92148,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.745154,
                                "cost_per_d7_retention": 13.145226,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":111,
                            }
                        }
                    ]
                },
                {
                    "opt_budget": 1000,
                    "solved": True,
                    "goal_improvement":-1,
                    "total": {
                        "original": {
                            "budget": 1000,
                            "media_budget":999,
                            "bid": 10,
                            "spend": 1000,
                            "installs": 620.29926,
                            "cpi": 1.086603,
                            "cpr": 1.0867368,
                            "registers": 767.3466,
                            "cohort_register_rate": 0.6232896,
                            "d1_cohort_register_rate": 0.4893754,
                            "d2_retention_rate": 0.50342476,
                            "d7_retention_rate": 0.10427435,
                            "cost_per_d2_retention": 2.5886462,
                            "cost_per_d7_retention": 12.497568,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d2_roas": 1,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                        },
                        "opt": {
                            "budget": 1000,
                            "bid": 10,
                            "spend": 1000,
                            "installs": 920.1288,
                            "cpi": 1.0868044,
                            "cpr": 1.0867368,
                            "registers": 767.282,
                            "cohort_register_rate": 0.6233334,
                            "d1_cohort_register_rate": 0.48940673,
                            "d2_retention_rate": 0.5034369,
                            "d7_retention_rate": 0.10427771,
                            "cost_per_d2_retention": 2.5888019,
                            "cost_per_d7_retention": 12.498218,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d2_roas": 1,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                            "media_budget":111,
                        }
                    },
                    "details": [
                        {
                            "campaign_name": "Google-FR-AND-220520-UAC2.5-purchase-lanhan-sdk-newinstall-WEU",
                            "portrait": ["fresh", "cost_wave", "cpi_wave", "not_enough_spend", "compete"],
                            "original": {
                                "budget": 2070.3813,
                                "bid": 24.11,
                                "spend": 2070.3813,
                                "installs": 2044.3282,
                                "cpi": 1.0127441,
                                "cpr": 1.0867368,
                                "registers": 1641.3597,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5288177,
                                "cost_per_d7_retention": 12.247065,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":444,
                            },
                            "opt": {
                                "budget": 706,
                                "bid": 24.11,
                                "spend": 706,
                                "installs": 697.1159,
                                "cpi": 1.0127441,
                                "cpr": 1.0867368,
                                "registers": 559.7037,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5288117,
                                "cost_per_d7_retention": 12.246924,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":111,
                            }
                        },
                        {
                            "campaign_name": "Google-FR-AND-220524-UAC2.5-purchase_ggsa-lanhan-sdk-newinstall-WEU",
                            "portrait": ["fresh", "cost_wave", "cpi_wave", "not_enough_spend", "compete"],
                            "original": {
                                "budget": 862.1701,
                                "bid": 24.11,
                                "spend": 862.1701,
                                "installs": 653.99664,
                                "cpi": 1.3183095,
                                "cpr": 1.0867368,
                                "registers": 608.7342,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.745177,
                                "cost_per_d7_retention": 13.145761,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":444,
                            },
                            "opt": {
                                "budget": 294,
                                "bid": 24.11,
                                "spend": 294,
                                "installs": 223.01286,
                                "cpi": 1.3183095,
                                "cpr": 1.0867368,
                                "registers": 207.57835,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.7451603,
                                "cost_per_d7_retention": 13.145372,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":111,
                            }
                        }
                    ]
                },
                {
                    "opt_budget": 500,
                    "solved": True,
                    "goal_improvement":0.01391,
                    "total": {
                        "original": {
                            "budget": 500,
                            "bid": 1,
                            "spend":-800,
                            "installs": 436.23944,
                            "cpi": 1.086603,
                            "cpr": 1.0867368,
                            "registers": 613.8773,
                            "cohort_register_rate": 0.6232896,
                            "d1_cohort_register_rate": 0.4893754,
                            "d2_retention_rate": 0.50342476,
                            "d7_retention_rate": 0.10427435,
                            "cost_per_d2_retention": 2.5886445,
                            "cost_per_d7_retention": 12.497529,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d2_roas": 1,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                            "media_budget":111,
                        },
                        "opt": {
                            "budget": 500,
                            "bid": 0,
                            "spend": 800,
                            "installs": 736.1488,
                            "cpi": 1.0867368,
                            "cpr": 1.0867368,
                            "registers": 613.84296,
                            "cohort_register_rate": 0.62331873,
                            "d1_cohort_register_rate": 0.4893962,
                            "d2_retention_rate": 0.50343287,
                            "d7_retention_rate": 0.10427658,
                            "cost_per_d2_retention": 2.5887477,
                            "cost_per_d7_retention": 12.49796,
                            "reattributions": 0,
                            "d1_retention_rate": 0,
                            "d14_retention_rate": 0,
                            "d1_roas": 0,
                            "d2_roas": 1,
                            "d3_roas": 0,
                            "d7_roas": 0,
                            "d14_roas": 0,
                            "cost_per_d1_retention": 0,
                            "cost_per_d14_retention": 0,
                            "media_budget":111,
                        }
                    },
                    "details": [
                        {
                            "campaign_name": "Google-FR-AND-220520-UAC2.5-purchase-lanhan-sdk-newinstall-WEU",
                            "portrait": [],
                            "original": {
                                "budget": 1325.5132,
                                "bid": 25.11,
                                "spend":-1325.5132,
                                "installs": 1308.8334,
                                "cpi": 1.0127441,
                                "cpr": 1.0867368,
                                "registers": 1050.8422,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5288157,
                                "cost_per_d7_retention": 12.247024,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":444,
                            },
                            "opt": {
                                "budget": 565,
                                "bid": 24.11,
                                "spend": 565,
                                "installs": 557.8902,
                                "cpi": 1.0127441,
                                "cpr": 1.0867368,
                                "registers": 447.92148,
                                "cohort_register_rate": 0.80288464,
                                "d1_cohort_register_rate": 0.47788462,
                                "d2_retention_rate": 0.4988024,
                                "d7_retention_rate": 0.10299401,
                                "cost_per_d2_retention": 2.5288093,
                                "cost_per_d7_retention": 12.246872,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":1111,
                            }
                        },
                        {
                            "campaign_name": "Google-FR-AND-220524-UAC2.5-purchase_ggsa-lanhan-sdk-newinstall-WEU",
                            "portrait": ["fresh", "cost_wave", "cpi_wave", "not_enough_spend", "compete"],
                            "original": {
                                "budget": 55190.31964,
                                "bid": 24.11,
                                "spend": 3055111.31964,
                                "installs": 418.20197,
                                "cpi": 1.3183095,
                                "cpr": 1.0867368,
                                "registers": 389.2586,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.7451723,
                                "cost_per_d7_retention": 13.145647,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":444,
                            },
                            "opt": {
                                "budget": 235,
                                "bid": 24.11,
                                "spend": 235,
                                "installs": 178.25858,
                                "cpi": 1.3183095,
                                "cpr": 1.0867368,
                                "registers": 165.92148,
                                "cohort_register_rate": 0.93079096,
                                "d1_cohort_register_rate": 0.5254237,
                                "d2_retention_rate": 0.5159332,
                                "d7_retention_rate": 0.107739,
                                "cost_per_d2_retention": 2.745154,
                                "cost_per_d7_retention": 13.145226,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                                "media_budget":111,
                            }
                        }
                    ]
                },
            ]
        }
    )


@app.route('/api/v1/portal/automation/opt_query', methods=['POST'])
def opt_query():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data": {
            "2023-03-08": {
                "value": [
                    {
                        "opt_budget": 1000,
                        "solved": True,
                        "total": {
                            "original": {
                                "budget": 1000,
                                "bid": 0,
                                "spend": 1000,
                                "installs": 946.2779,
                                "cpi": 1.056772,
                                "cpr": 1.056772,
                                "registers": 804.60583,
                                "cohort_register_rate": 0.6421281,
                                "d1_cohort_register_rate": 0,
                                "d2_retention_rate": 0.49315867,
                                "d7_retention_rate": 0.09908504,
                                "cost_per_d2_retention": 0.49315867,
                                "cost_per_d7_retention": 0.09908504,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                            },
                            "opt": {
                                "budget": 1000,
                                "bid": 0,
                                "spend": 1000,
                                "installs": 946.1006,
                                "cpi": 1.0569701,
                                "cpr": 1.0569701,
                                "registers": 804.5332,
                                "cohort_register_rate": 0.64216506,
                                "d1_cohort_register_rate": 0,
                                "d2_retention_rate": 0.49314678,
                                "d7_retention_rate": 0.09908905,
                                "cost_per_d2_retention": 0.49314678,
                                "cost_per_d7_retention": 0.09908905,
                                "reattributions": 0,
                                "d1_retention_rate": 0,
                                "d14_retention_rate": 0,
                                "d1_roas": 0,
                                "d2_roas": 1,
                                "d3_roas": 0,
                                "d7_roas": 0,
                                "d14_roas": 0,
                                "cost_per_d1_retention": 0,
                                "cost_per_d14_retention": 0,
                            }
                        },
                        "details": [
                            {
                                "campaign_name": "Google-FR-AND-220520-UAC2.5-purchase-lanhan-sdk-newinstall-WEU",
                                "portrait": ["fresh", "cost_wave", "cpi_wave", "not_enough_spend", "compete"],
                                "original": {
                                    "budget": 2070.3813,
                                    "bid": 24.11,
                                    "spend": 2070.3813,
                                    "installs": 2103.7092,
                                    "cpi": 0.9841575,
                                    "cpr": 1.0569701,
                                    "registers": 1725.0416,
                                    "cohort_register_rate": 0.82,
                                    "d1_cohort_register_rate": 0.4961905,
                                    "d2_retention_rate": 0.49767712,
                                    "d7_retention_rate": 0.09756097,
                                    "cost_per_d2_retention": 2.4115849,
                                    "cost_per_d7_retention": 12.301895,
                                    "reattributions": 0,
                                    "d1_retention_rate": 0,
                                    "d14_retention_rate": 0,
                                    "d1_roas": 0,
                                    "d2_roas": 1,
                                    "d3_roas": 0,
                                    "d7_roas": 0,
                                    "d14_roas": 0,
                                    "cost_per_d1_retention": 0,
                                    "cost_per_d14_retention": 0,
                                },
                                "opt": {
                                    "budget": 706,
                                    "bid": 24.11,
                                    "spend": 706,
                                    "installs": 717.36487,
                                    "cpi": 0.9841575,
                                    "cpr": 1.0569701,
                                    "registers": 588.2392,
                                    "cohort_register_rate": 0.82,
                                    "d1_cohort_register_rate": 0.4961905,
                                    "d2_retention_rate": 0.49767712,
                                    "d7_retention_rate": 0.09756097,
                                    "cost_per_d2_retention": 2.4115796,
                                    "cost_per_d7_retention": 12.301754,
                                    "reattributions": 0,
                                    "d1_retention_rate": 0,
                                    "d14_retention_rate": 0,
                                    "d1_roas": 0,
                                    "d2_roas": 1,
                                    "d3_roas": 0,
                                    "d7_roas": 0,
                                    "d14_roas": 0,
                                    "cost_per_d1_retention": 0,
                                    "cost_per_d14_retention": 0,
                                }
                            },
                            {
                                "campaign_name": "Google-FR-AND-220524-UAC2.5-purchase_ggsa-lanhan-sdk-newinstall-WEU",
                                "portrait": ["fresh", "cost_wave", "cpi_wave"],
                                "original": {
                                    "budget": 862.1701,
                                    "bid": 24.11,
                                    "spend": 862.1701,
                                    "installs": 670.7792,
                                    "cpi": 1.2853262,
                                    "cpr": 1.0569701,
                                    "registers": 634.2933,
                                    "cohort_register_rate": 0.9456067,
                                    "d1_cohort_register_rate": 0.53974897,
                                    "d2_retention_rate": 0.48082596,
                                    "d7_retention_rate": 0.10324484,
                                    "cost_per_d2_retention": 2.8269198,
                                    "cost_per_d7_retention": 13.165212,
                                    "reattributions": 0,
                                    "d1_retention_rate": 0,
                                    "d14_retention_rate": 0,
                                    "d1_roas": 0,
                                    "d2_roas": 1,
                                    "d3_roas": 0,
                                    "d7_roas": 0,
                                    "d14_roas": 0,
                                    "cost_per_d1_retention": 0,
                                    "cost_per_d14_retention": 0,
                                },
                                "opt": {
                                    "budget": 294,
                                    "bid": 24.11,
                                    "spend": 294,
                                    "installs": 228.7357,
                                    "cpi": 1.2853262,
                                    "cpr": 1.0569701,
                                    "registers": 216.29402,
                                    "cohort_register_rate": 0.9456067,
                                    "d1_cohort_register_rate": 0.53974897,
                                    "d2_retention_rate": 0.48082596,
                                    "d7_retention_rate": 0.10324484,
                                    "cost_per_d2_retention": 2.826902,
                                    "cost_per_d7_retention": 13.164824,
                                    "reattributions": 0,
                                    "d1_retention_rate": 0,
                                    "d14_retention_rate": 0,
                                    "d1_roas": 0,
                                    "d2_roas": 1,
                                    "d3_roas": 0,
                                    "d7_roas": 0,
                                    "d14_roas": 0,
                                    "cost_per_d1_retention": 0,
                                    "cost_per_d14_retention": 0,
                                }
                            }
                        ]
                    }
                ]
            }
        }
    })


@app.route('/api/v1/portal/assistants', methods=['POST'])
def assistants():
    print(flask.request.json)
    with open('assistants.json', 'r', encoding='utf8') as f:
        content = json.load(f)
    return flask.jsonify(content)

# @app.route('/predict/', methods=['POST'])
# def comment_valid():
#     print(flask.request.json)
#     return flask.jsonify({
#         "data": {
#             "contents": [
#                 "#TowerofFantasy #Tofgether #NewEra #Cherimu"
#             ],
#             "isvalid": [
#                 0
#             ]
#         },
#         "message": "success",
#         "ret_code": "0",
#         "session_data": {}
#     })


@app.route('/predict/', methods=['POST'])
def keywords_cluster():
    print(flask.request.json)
    return flask.jsonify({
        "data": "{\"adc\": [\"2 adc\", \"with an adc\", \"juego al shooter\", \"adc 1v1\", \"ass adc\", \"shooter\", \"- adc\", \"cda6\", \"シューティングが身\", \"adc i'll\", \"adc adc\", \"dois adc\", \"nişancıya\", \"adc me\", \"游戏搭子射手\", \"shooter game\", \"شوتر\", \"az adc\", \"arkeiro tenho\", \"ja adc\", \"adc are the\", \"adc var\", \"game adc\", \"adc de dos\", \"1v1 the adc\", \"adc it's\", \"000 adc\", \"adc3\", \"me adc\", \"of adc\", \"best adc\", \"on adc\", \"5 atirador\", \"3 atiradores\", \"adc ass\", \"arqueiros\", \"adc lol\", \"0 adc's\", \"アーチャー\", \"had 4 adc\", \"ter atirador\", \"v adc\", \"adc game\", \"na adc\", \"jugar shooters\", \"og shooter\", \"tinha 4 adc\", \"adc bro\", \"shooters\", \"as an adc\", \"had adc\", \"having an adc\", \"be an adc\", \"esses adc\", \"nosso adc\", \"cda 0\", \"and adc are\", \"marksmana\", \"3300 4566 8173 adc\", \"adc pls\", \"desses adc\", \"-adc\", \"juego shooter\", \"an adc\", \"joga de adc\", \"槍手\", \"marksman yang\", \"6 adc\", \"adc are\", \"mi adc\", \"juegos de shooter\", \"and adc\", \"adc solo\", \"if the adc\", \"adc's\", \"1 adc\", \"be a adc\", \"archer\", \"marksman\", \"have a adc\", \"adc has\", \"adc is okay\", \"4adc\", \"2 adcs\", \"adc that\", \"juego de shooters\", \"adc6\", \"jogo de adc\", \"marksmen\", \"10 adc\", \"have an adc\", \"jestem adc\", \"射手\", \"arqueiro\", \"oyun adc\", \"adc je je\", \"lol adc\", \"shooter oyunu\", \"有射手\", \"3adc\", \"adc 3v1\", \"adcs\", \"be adc\", \"el adc\", \"adc oyunu\", \"00 adc\", \"adc 2v1\", \"3 adc\", \"be the adc\", \"adc for\", \"adc 's\", \"sou adc\", \"been an adc\", \"adc del juego\", \"2adc\", \"aquele adc\", \"弓箭手\", \"euw adc\", \"1v1 an adc\", \"los adc\", \"adc - lol\", \"4 atiradores\", \"adc is\", \"atiradores\", \"3 tiradores\", \"tem um adc\", \"adc by\", \"arqueiras\", \"adc okay\", \"dia adc\", \"adc ta\", \"qualquer adc\", \"0 adc\", \"dos tiradores\", \"juegos de disparos\", \"adc\", \"adc i\", \"para adc\", \"撃ちの子\", \"adc you're\", \"枪手\", \"como adc\", \"het cda\", \"4 adc\", \"jugar un shooter\", \"adc lan\", \"uit cda\", \"tinha 2 adc\", \"an adc that\", \"nişancılar\", \"jogar de adc\", \"adc and\", \"jogo adc\", \"the adc\", \"cda\", \"4射手\", \"esse adc\", \"vs adc\", \"5 adc\", \"our adc\", \"2023 adc\", \"for adc\", \"adc main\", \"melhor adc\", \"jugar adc\", \"3射手\", \"#adc\"]}",
        "message": "success",
        "ret_code": "0",
        "session_data": {}
    })
    # return flask.jsonify({
    #     "data": {
    #         "adc": "adc"
    #     },
    #     "message": "success",
    #     "ret_code": "0",
    #     "session_data": {}
    # })


@app.route('/api/v1/portal/interface_list', methods=['POST'])
def interface_list():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "id": 9,
                    "name": "语种识别",
                    "url": "http://101.32.107.175:8000/api/v1/opinion_language_detection",
                    "protocol": "POST",
                    "headers": [],
                    "body": "{\r\n    \"content\": [\r\n        \"this game lag too much! please fix it!\"\r\n    ]\r\n}",
                    "result": "",
                    "time": 0,
                    "create_time": "2023-03-17 12:45:03 +0800 CST"
                },
                {
                    "id": 8,
                    "name": "test-assistants-szp",
                    "url": "http://43.134.152.100:8080/api/v1/portal/assistants",
                    "protocol": "POST",
                    "headers": [],
                    "body": "{\r\n    \"game_code\": \"nikke\",\r\n    \"dtstatdate\": \"2023-03-11\"\r\n}",
                    "result": "{\"data\":{\"value_1_list\":[],\"value_2_list\":[]},\"message\":\"Success\",\"ret_code\":\"0\"}",
                    "time": 61,
                    "create_time": "2023-03-17 12:21:33 +0800 CST"
                },
                {
                    "id": 7,
                    "name": "语种识别",
                    "url": "http://101.32.107.175:8000/api/v1/opinion_language_detection",
                    "protocol": "POST",
                    "headers": [],
                    "body": "{\r\n    \"content\": [\r\n        \"this game lag too much! please fix it!\"\r\n    ]\r\n}",
                    "result": "",
                    "time": 0,
                    "create_time": "2023-03-16 12:45:03 +0800 CST"
                },
                {
                    "id": 6,
                    "name": "test-assistants-szp",
                    "url": "http://43.134.152.100:8080/api/v1/portal/assistants",
                    "protocol": "POST",
                    "headers": [],
                    "body": "{\r\n    \"game_code\": \"nikke\",\r\n    \"dtstatdate\": \"2023-03-11\"\r\n}",
                    "result": "{\"data\":{\"value_1_list\":[],\"value_2_list\":[]},\"message\":\"Success\",\"ret_code\":\"0\"}",
                    "time": 61,
                    "create_time": "2023-03-16 12:21:33 +0800 CST"
                },
                {
                    "id": 4,
                    "name": "test-assistants-jacc",
                    "url": "http://43.134.152.100:8080/api/v1/portal/assistants",
                    "protocol": "POST",
                    "headers": [],
                    "body": "{\r\n    \"game_code\": \"nikke\",\r\n    \"dtstatdate\": \"2023-03-10\"\r\n}",
                    "result": "{\"data\":{\"value_1_list\":[],\"value_2_list\":[]},\"message\":\"Success\",\"ret_code\":\"0\"}",
                    "time": 1194,
                    "create_time": "2023-03-16 10:52:56 +0800 CST"
                },
                {
                    "id": 3,
                    "name": "test-assistants-again1",
                    "url": "http://43.134.152.100:8080/api/v1/portal/assistants",
                    "protocol": "POST",
                    "headers": [],
                    "body": "{\r\n    \"game_code\": \"nikke\",\r\n    \"dtstatdate\": \"2023-03-10\"\r\n}",
                    "result": "{\"data\":{\"value_1_list\":[],\"value_2_list\":[]},\"message\":\"Success\",\"ret_code\":\"0\"}",
                    "time": 467,
                    "create_time": "2023-03-16 10:45:52 +0800 CST"
                }
            ]
        }
    )


@app.route('/api/v1/portal/automation/user_game_code', methods=['POST'])
def user_game_code():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "success",
            "data":
                {
                    "game_codes": ["nikke", "pubgm"]
                }
        }
    )


@app.route('/api/v1/portal/summary_sentence_details', methods=['POST'])
def summary_sentence_details():
    print(flask.request.json)
    with open('summary_sentence_details.json', 'r', encoding='utf8') as f:
        content = json.load(f)
    return flask.jsonify(content)


@app.route('/api/v1/portal/summary_sentence_comments', methods=['POST'])
def summary_sentence_comments():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "md5_uin": "8b6bb19102431e7ef7c360444066d5bc",
                    "content": "回复 @imransenyum\nHahahaha rank hanya ilusi. Jom im gi beta honor of kings. Sumpah semua gempak",
                    "content_to_zh": "回复@imransenyum hahahaha 排名只是一种幻觉。让我们去王者荣耀公测吧。我发誓一切都很吵",
                    "content_to_en": "回复 @imransenyum hahahaha rank is just an illusion. let's go to the honor of kings beta. i swear everything is loud"
                },
                {
                    "md5_uin": "1085179992171888640",
                    "content": "No mais alto nível de hok,jg é o 7° em ranking de banimentos.",
                    "content_to_zh": "在最高级别的hok中，jg在ban排名中排名第7。",
                    "content_to_en": "at the highest level of hok, jg is 7th in ban ranking."
                },
                {
                    "md5_uin": "1085014994216828948",
                    "content": "Galera, selecionei meu estado errado lá no rank, tem como alterar ?",
                    "content_to_zh": "伙计们，我在排名中选择了我的状态，我可以更改它吗？",
                    "content_to_en": "guys, i selected my state wrong there in the rank, can i change it?"
                },
                {
                    "md5_uin": "2008f71988e27cc7a21c2f25a2929ec8",
                    "content": "回复 @HoK_BR\nola, boa tarde.\n\nGostaria de fazer uma observação que creio eu que 99% dos jogadores de HoK vai concordar, está muito difícil jogar rankeada abaixo do rank diamante pelo fato de você não poder escolher sua rota fixa e cair nela quando começa a escolha de campeão +",
                    "content_to_zh": "回复@hok_br 你好，下午好。我想做一个观察，相信99%的hok玩家都会同意，钻石段位以下的段位很难玩，因为你不能选择你的固定路线，开始选择冠军的时候就掉进去了",
                    "content_to_en": "回复 @hok_br hello, good afternoon. i would like to make an observation that i believe 99% of hok players will agree, it is very difficult to play ranked below the diamond rank because you cannot choose your fixed route and fall into it when the champion choice begins"
                },
                {
                    "md5_uin": "1085053688151822406",
                    "content": "Alguém aí manda print de como está o ranking, por favor?",
                    "content_to_zh": "有没有人发送一份排名如何的印刷品？",
                    "content_to_en": "does anyone send a print of how the ranking is, please?"
                },
                {
                    "md5_uin": "1085007238206341200",
                    "content": "Rank servidor rota",
                    "content_to_zh": "路由服务器排名",
                    "content_to_en": "route server rank"
                },
                {
                    "md5_uin": "1085066198888230912",
                    "content": "Angela se for pra subir rank",
                    "content_to_zh": "pra subir rank 的安琪拉 se",
                    "content_to_en": "angela se for pra subir rank"
                },
                {
                    "md5_uin": "1084904056759275670",
                    "content": "Hiro se você cair com troll na rank você pode banir?",
                    "content_to_zh": "hiro 如果你在 rank 中掉到 troll 你能 ban 吗？",
                    "content_to_en": "hiro if you fall with troll in rank can you ban?"
                },
                {
                    "md5_uin": "1085226214530236476",
                    "content": "Broxei quando cheguei no dima lá só os pateta na rank",
                    "content_to_zh": "当我到达 dima 时我感到无聊，队伍中只有愚蠢的人",
                    "content_to_en": "i got bored when i got to dima, there were only the goofy ones in the rank"
                },
                {
                    "md5_uin": "1084951571823071393",
                    "content": "alguém ranking dima querendo jogar ?",
                    "content_to_zh": "有人排名 dima 想玩吗？",
                    "content_to_en": "anyone ranking dima wanting to play?"
                },
                {
                    "md5_uin": "1084942605571330089",
                    "content": "Vai fazer parte dos 90% de adc que cai na minha rank",
                    "content_to_zh": "将成为我排名中90％的adc的一部分",
                    "content_to_en": "will be part of the 90% of adc that falls in my rank"
                },
                {
                    "md5_uin": "1084985331159404555",
                    "content": "Alguém rank subir diamante trio",
                    "content_to_zh": "有人给钻石三重奏排名",
                    "content_to_en": "someone rank up diamond trio"
                }
            ]
        }
    )


@app.route('/api/v1/portal/summary_modify_sentence', methods=['POST'])
def summary_modify_sentence():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "success"
        }
    )


@app.route('/api/v1/portal/summary_del_sentence', methods=['POST'])
def summary_del_sentence():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "success"
        }
    )


@app.route('/api/v1/portal/summary_recover_sentence', methods=['POST'])
def summary_recover_sentence():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "success"
        }
    )


@app.route('/api/v1/portal/summary_params', methods=['GET'])
def summary_params():
    print(flask.request.form)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": {
                "channel_type": {
                    "value": [
                        {
                            "label": "total",
                            "value": "total"
                        },
                        {
                            "label": "comments",
                            "value": "comments"
                        },
                        {
                            "label": "social",
                            "value": "social"
                        }
                    ]
                },
                "data_language": {
                    "value": [
                        {
                            "label": "all",
                            "value": "all"
                        },
                        {
                            "label": "es",
                            "value": "es"
                        },
                        {
                            "label": "pt",
                            "value": "pt"
                        },
                        {
                            "label": "en",
                            "value": "en"
                        },
                        {
                            "label": "zh",
                            "value": "zh"
                        }
                    ]
                },
                "data_sentiment": {
                    "value": [
                        {
                            "label": "total",
                            "value": "total"
                        },
                        {
                            "label": "negative",
                            "value": "negative"
                        },
                        {
                            "label": "positive",
                            "value": "positive"
                        }
                    ]
                },
                "game": {
                    "value": [
                        {
                            "label": "幻塔",
                            "value": "u6d721eb69ef7de198bb84be26be6d40b|"
                        },
                        {
                            "label": "HOK/AOV",
                            "value": "u10000000066|"
                        },
                        {
                            "label": "PUBG",
                            "value": "ufc454d9b1af70b40588e2a6fa4da4a8b|"
                        },
                        {
                            "label": "NIKKE",
                            "value": "uef4312b08dde07820374dd57086ea2fb|"
                        },
                        {
                            "label": "Warhammer 40,000: Darktide",
                            "value": "u72b4feda779c36a6b6d3cb5eb8efe5d1|"
                        },
                        {
                            "label": "阿凡达-蓝色行动",
                            "value": "u10000000033|"
                        },
                        {
                            "label": "SOP 重生边缘",
                            "value": "uaccc6f302cd02c7e0cf7c806497a3395|"
                        },
                        {
                            "label": "Vrising",
                            "value": "uc41360495e0a6b2eb0809ded33746044|"
                        },
                        {
                            "label": "ACM刺客信条",
                            "value": "u22eae55990dfe9ef2932e5a8234d63db|"
                        },
                        {
                            "label": "黎明觉醒（生机/Undawn）",
                            "value": "u037857a0ad6aaad86a15227be23adcc4|"
                        },
                        {
                            "label": "NBA2",
                            "value": "u03e9e2775cf377904ca6583456d9f411|"
                        },
                        {
                            "label": "Genshin Impact",
                            "value": "uf0a4c651423effde0425337ca0a2fd51|"
                        },
                        {
                            "label": "MLBB",
                            "value": "u1426b49d8626e915264442d821e41a4e|"
                        },
                        {
                            "label": "UAMO",
                            "value": "u10000000022|"
                        },
                        {
                            "label": "RE0",
                            "value": "u10000000030|"
                        },
                        {
                            "label": "Nightingale",
                            "value": "|e11000000297"
                        },
                        {
                            "label": "Bloodhunt",
                            "value": "|e00000000001"
                        }
                    ]
                }
            }
        }
    )


@app.route('/api/v1/portal/associated_first_words', methods=['POST'])
def associated_first_words():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "word": "do",
                    "count": 211,
                    "word_to_en": "do",
                    "word_to_zh": "做"
                },
                {
                    "word": "have",
                    "count": 157,
                    "word_to_en": "have",
                    "word_to_zh": "有"
                },
                {
                    "word": "get",
                    "count": 95,
                    "word_to_en": "get",
                    "word_to_zh": "得到"
                },
                {
                    "word": "are",
                    "count": 79,
                    "word_to_en": "are",
                    "word_to_zh": "是"
                },
                {
                    "word": "use",
                    "count": 73,
                    "word_to_en": "use",
                    "word_to_zh": "使用"
                },
                {
                    "word": "play",
                    "count": 68,
                    "word_to_en": "play",
                    "word_to_zh": "玩"
                },
                {
                    "word": "good",
                    "count": 66,
                    "word_to_en": "good",
                    "word_to_zh": "好的"
                },
                {
                    "word": "'m",
                    "count": 65,
                    "word_to_en": "'m",
                    "word_to_zh": "我"
                },
                {
                    "word": "game",
                    "count": 63,
                    "word_to_en": "game",
                    "word_to_zh": "游戏"
                },
                {
                    "word": "go",
                    "count": 63,
                    "word_to_en": "go",
                    "word_to_zh": "去"
                },
                {
                    "word": "need",
                    "count": 60,
                    "word_to_en": "need",
                    "word_to_zh": "需要"
                },
                {
                    "word": "armory",
                    "count": 48,
                    "word_to_en": "armory",
                    "word_to_zh": "军械库"
                },
                {
                    "word": "nt",
                    "count": 47,
                    "word_to_en": "nt",
                    "word_to_zh": "新台币"
                },
                {
                    "word": "time",
                    "count": 46,
                    "word_to_en": "time",
                    "word_to_zh": "时间"
                },
                {
                    "word": "sell",
                    "count": 43,
                    "word_to_en": "sell",
                    "word_to_zh": "卖"
                },
                {
                    "word": "valley",
                    "count": 42,
                    "word_to_en": "valley",
                    "word_to_zh": "谷"
                },
                {
                    "word": "know",
                    "count": 42,
                    "word_to_en": "know",
                    "word_to_zh": "知道"
                },
                {
                    "word": "m",
                    "count": 40,
                    "word_to_en": "m",
                    "word_to_zh": "米"
                },
                {
                    "word": "anyone",
                    "count": 39,
                    "word_to_en": "anyone",
                    "word_to_zh": "任何人"
                },
                {
                    "word": "full",
                    "count": 38,
                    "word_to_en": "full",
                    "word_to_zh": "满的"
                },
                {
                    "word": "i",
                    "count": 37,
                    "word_to_en": "i",
                    "word_to_zh": "我"
                },
                {
                    "word": "run",
                    "count": 36,
                    "word_to_en": "run",
                    "word_to_zh": "跑步"
                },
                {
                    "word": "bro",
                    "count": 35,
                    "word_to_en": "bro",
                    "word_to_zh": "兄弟"
                },
                {
                    "word": "make",
                    "count": 35,
                    "word_to_en": "make",
                    "word_to_zh": "制作"
                },
                {
                    "word": "loot",
                    "count": 34,
                    "word_to_en": "loot",
                    "word_to_zh": "抢劫"
                },
                {
                    "word": "armor",
                    "count": 33,
                    "word_to_en": "armor",
                    "word_to_zh": "盔甲"
                },
                {
                    "word": "one",
                    "count": 33,
                    "word_to_en": "one",
                    "word_to_zh": "一"
                },
                {
                    "word": "kill",
                    "count": 33,
                    "word_to_en": "kill",
                    "word_to_zh": "杀"
                },
                {
                    "word": "think",
                    "count": 32,
                    "word_to_en": "think",
                    "word_to_zh": "思考"
                },
                {
                    "word": "people",
                    "count": 32,
                    "word_to_en": "people",
                    "word_to_zh": "人们"
                },
                {
                    "word": "same",
                    "count": 31,
                    "word_to_en": "same",
                    "word_to_zh": "相同的"
                },
                {
                    "word": "guys",
                    "count": 30,
                    "word_to_en": "guys",
                    "word_to_zh": "伙计们"
                },
                {
                    "word": "want",
                    "count": 30,
                    "word_to_en": "want",
                    "word_to_zh": "想"
                },
                {
                    "word": "see",
                    "count": 30,
                    "word_to_en": "see",
                    "word_to_zh": "看"
                },
                {
                    "word": "other",
                    "count": 29,
                    "word_to_en": "other",
                    "word_to_zh": "其他"
                },
                {
                    "word": "much",
                    "count": 28,
                    "word_to_en": "much",
                    "word_to_zh": "很多"
                },
                {
                    "word": "someone",
                    "count": 27,
                    "word_to_en": "someone",
                    "word_to_zh": "某人"
                },
                {
                    "word": "take",
                    "count": 25,
                    "word_to_en": "take",
                    "word_to_zh": "拿"
                },
                {
                    "word": "stuff",
                    "count": 25,
                    "word_to_en": "stuff",
                    "word_to_zh": "东西"
                },
                {
                    "word": "ammo",
                    "count": 24,
                    "word_to_en": "ammo",
                    "word_to_zh": "弹药"
                },
                {
                    "word": "wanna",
                    "count": 24,
                    "word_to_en": "wanna",
                    "word_to_zh": "想"
                },
                {
                    "word": "give",
                    "count": 23,
                    "word_to_en": "give",
                    "word_to_zh": "给"
                },
                {
                    "word": "guy",
                    "count": 23,
                    "word_to_en": "guy",
                    "word_to_zh": "家伙"
                },
                {
                    "word": "players",
                    "count": 23,
                    "word_to_en": "players",
                    "word_to_zh": "球员"
                },
                {
                    "word": "new",
                    "count": 22,
                    "word_to_en": "new",
                    "word_to_zh": "新的"
                },
                {
                    "word": "gear",
                    "count": 22,
                    "word_to_en": "gear",
                    "word_to_zh": "齿轮"
                },
                {
                    "word": "first",
                    "count": 21,
                    "word_to_en": "first",
                    "word_to_zh": "第一的"
                },
                {
                    "word": "'re",
                    "count": 21,
                    "word_to_en": "'re",
                    "word_to_zh": "&#39;关于"
                },
                {
                    "word": "am",
                    "count": 20,
                    "word_to_en": "am",
                    "word_to_zh": "是"
                },
                {
                    "word": "find",
                    "count": 20,
                    "word_to_en": "find",
                    "word_to_zh": "寻找"
                }
            ]
        }
    )


@app.route('/api/v1/portal/associated_first_word_comments', methods=['POST'])
def associated_first_word_comments():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": {
                "comments": [
                    {
                        "content": "Don't sweat it",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Bro i dont think i have space for more then 2 🗿",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Don't worry nothing special, 10 win streak, 1 die , 3 wins , 1 lose",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "i dont have a headphone for my pc",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Just don't mind me I'm looking for people from my country",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "cn players knifing me like bro im not a dog don't put me on your dinner table",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Does it have something to do with material",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "how many hours played do you guys have?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Prolly gl4 at max just to make sure funni deaths dont ruin the dazzle xD",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I remember had a team trynna kill a duo here i really recommend them to not try that cuz im using us round and the enemy were using T5 armour they do it anyways and we all diee i had to join them cuz if not i will be insulted",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "imma do a naked armory run",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Dont give a gay answer",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "We don't eat tacos",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Uhh well here's the problem I don't have space to expand rigs <:moaistoneab:1086377050144780339>",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Do the wiggle and you're safe",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "To aware of certain conditions and do whatever the heck you want during combat phase",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Sell what you don't use",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Fr, I'm not that good, the only way I can extract from armory is if I don't go inside the armory 💀",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "my team was fighting over a suppressor 🤣🤣🤣 little do they know i was the one who rushed the fker and fked em up",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "What do you guys think of Renoir?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I kind of don't want, because my friends are starting to level up, so i kind of need the high tier gear, and low gear foe rats runs",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "anyone wanna do farm or valley?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Nah\nNo way its trash\nI mean cmon it look so good\nUnless u dont waste tons of money",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Irl they dont",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I think you only have 4 hours to do that",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Hope they don't find it 🥲",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "It's ok if I dont like the fal",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Hopefully the devs do partial or just give everyone the same loot after",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Do you have any longer~ gameplay in same conditions?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Ik u mean like show u down but they don't it like a mini flash bang",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I wanna do armory task but imma just die if I go there",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "And you dont lose your mag this way",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I don't know if you're also furry\nIdk haven't played genshin yet",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Mexican speaks spanish we don't speak spanish bro",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Wanna do team?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "*raise hand*\n\nWould backpacks do good? I didn't had much money now. Really need to get those missing 220k back and get myself to 600k area again",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Still broke and i don't have one",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Idek what to do anymore 💀 even if Im minding my own business I get sniped lmao.",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Don't wear or atleast don't wear tier 6 helmets that block sound they awful impractical a scav player can sneak on you kill you easily cause your overweight",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "i dont know honestly",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "How do you guys spell armoury with a U or without the U",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Gonna do an sks build tonight to",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Play it slow breh\nDont rush in\nOne of the most things that help me kill players is me hearing them first\nOnce you hear footsteps immediately crouch walk or slow walk that will reduce ur movement sound to green or yellow and just wait for them\nThats how i won most fights",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Most of us don't want to",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Anyone wanna do Manhunt?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "we dont loot till kill all scavs",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Do you have a laser on your gun?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "<@Mik> why you dont came back and grav my stuff",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I dont think u can jump like a bunny in tarkov and shot ppl",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I usually do but then I lose track of them if I do it with too many guns",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "BRO AT THIS POINT JUST DON'T PLAY THE GAME AT ALL💀",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "When i dont have gear i just get a backpack and do a naked run",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Lmao you also do naked sniper runs and kill t5-6 ppl ? 😂",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "ajax is annoying bro all i wanna do is pass through stables or motel and his squad light me up like chill mane",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Ok how much money cuz i don't see it",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "How much money do u have sugar daddy",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Which do you prefer to play most of the time?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "If your Christian do not be afraid of the dark for you have God on your side",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "mfs don't want to firefight with me now 😭😭",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I've never seen any color code when I check out the market for bullets. The color code only appears after I bought them. \n\nIs it common, or is it a bug? If it's common, why do they've done it differently?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Do y’all think they should remove the weekly listing limit?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Around afternoon? To night? Sometimes midnight haha cause I do most of my work in the morning",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "yeah i don't really care anymore if i die its just annoying",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Do you guys sell modified guns? Curious question",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "tip: don't fall for your ex.",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I don't wana show u the 18 secret documents now",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Where do y'all get this much valuable stuff tho",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Do u think it is lookalike?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Well,at least you don't need to wait for too long",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "<@Mik> u wanna do some ab",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Where do you get the Golden Deagle?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "You should do some give away frfr lol",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "why dont u use boxes?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I dont get to see my teamates getting head eyed",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Dont buy HK416",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "do you need a team or just solo",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "If u didnt do low footstep",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Anyone from eu wanna do manhunt? (Im bad)",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "how much memory space do i need to install arena breakout CN (chinese)?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Dont ask gow i gotnin",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "God.. We really need to have expensive gear on Armory? Dem... \n\nIdk how to do the covert mission where we put down the gunpowder\n\nLike.. Does out character will already carry it from start or not?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Oh wait forgot to do nitro giveaway",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "This is what i usually bring to raids. What do i need to change?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "U dont have the right to talk to me",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "What do you mean? They're the best leg destroyers",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Don't lie to me",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Ok but do u think the key was worth it",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I don't get it",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "i dont even know where to put your id",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Can ask  where do I open the 2 extraction on armoury",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Dont worry it drops sometimes",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Anyone wanna do a manhunt collab? I need loot and for quests 🥲",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "What do you guys think of Renoir?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "All i do is pvp",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "At least everyone has equal equipment. Plus you don't need to grind the gear",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Nope the thermal has limited range. I dont use it",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Just dont end up like the guys i kill",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Sell the ump mags if you don't use it <:moaistoneab:1086377050144780339>",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "yes, if i dont need the attachments",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "So im in the health section rn and i dont see quickheal",
                        "content_to_en": "",
                        "content_to_zh": ""
                    }
                ],
                "sentiment_rating": [
                    {
                        "name": "negative",
                        "value": 5
                    },
                    {
                        "name": "neutral",
                        "value": 94
                    },
                    {
                        "name": "positive",
                        "value": 1
                    }
                ]
            }
        }
    )


@app.route('/api/v1/portal/associated_second_words', methods=['POST'])
def associated_second_words():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "nt",
                    "tail_to_en": "nt",
                    "tail_to_zh": "新台币",
                    "count": 44
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "have",
                    "tail_to_en": "have",
                    "tail_to_zh": "有",
                    "count": 19
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "need",
                    "tail_to_en": "need",
                    "tail_to_zh": "需要",
                    "count": 12
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "use",
                    "tail_to_en": "use",
                    "tail_to_zh": "使用",
                    "count": 12
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "know",
                    "tail_to_en": "know",
                    "tail_to_zh": "知道",
                    "count": 11
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "get",
                    "tail_to_en": "get",
                    "tail_to_zh": "得到",
                    "count": 10
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "think",
                    "tail_to_en": "think",
                    "tail_to_zh": "思考",
                    "count": 9
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "guys",
                    "tail_to_en": "guys",
                    "tail_to_zh": "伙计们",
                    "count": 6
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "want",
                    "tail_to_en": "want",
                    "tail_to_zh": "想",
                    "count": 6
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "naked",
                    "tail_to_en": "naked",
                    "tail_to_zh": "裸",
                    "count": 5
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "see",
                    "tail_to_en": "see",
                    "tail_to_zh": "看",
                    "count": 4
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "like",
                    "tail_to_en": "like",
                    "tail_to_zh": "喜欢",
                    "count": 3
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "covert",
                    "tail_to_en": "covert",
                    "tail_to_zh": "隐蔽",
                    "count": 3
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "go",
                    "tail_to_en": "go",
                    "tail_to_zh": "去",
                    "count": 3
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "valley",
                    "tail_to_en": "valley",
                    "tail_to_zh": "谷",
                    "count": 3
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "play",
                    "tail_to_en": "play",
                    "tail_to_zh": "玩",
                    "count": 3
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "mind",
                    "tail_to_en": "mind",
                    "tail_to_zh": "头脑",
                    "count": 3
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "waste",
                    "tail_to_en": "waste",
                    "tail_to_zh": "浪费",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "ruin",
                    "tail_to_en": "ruin",
                    "tail_to_zh": "废墟",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "wanna",
                    "tail_to_en": "wanna",
                    "tail_to_zh": "想",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "speak",
                    "tail_to_en": "speak",
                    "tail_to_zh": "说话",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "do",
                    "tail_to_en": "do",
                    "tail_to_zh": "做",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "manhunt",
                    "tail_to_en": "manhunt",
                    "tail_to_zh": "追捕",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "worry",
                    "tail_to_en": "worry",
                    "tail_to_zh": "担心",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "run",
                    "tail_to_en": "run",
                    "tail_to_zh": "跑步",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "good",
                    "tail_to_en": "good",
                    "tail_to_zh": "好的",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "runs",
                    "tail_to_en": "runs",
                    "tail_to_zh": "跑",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "give",
                    "tail_to_en": "give",
                    "tail_to_zh": "给",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "armory",
                    "tail_to_en": "armory",
                    "tail_to_zh": "军械库",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "afraid",
                    "tail_to_en": "afraid",
                    "tail_to_zh": "害怕的",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "farm",
                    "tail_to_en": "farm",
                    "tail_to_zh": "农场",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "mean",
                    "tail_to_en": "mean",
                    "tail_to_zh": "意思是",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "take",
                    "tail_to_en": "take",
                    "tail_to_zh": "拿",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "nitro giveaway",
                    "tail_to_en": "nitro giveaway",
                    "tail_to_zh": "硝基赠品",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "thumbs",
                    "tail_to_en": "thumbs",
                    "tail_to_zh": "大拇指",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "lose",
                    "tail_to_en": "lose",
                    "tail_to_zh": "失去",
                    "count": 2
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "money",
                    "tail_to_en": "money",
                    "tail_to_zh": "钱",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "game",
                    "tail_to_en": "game",
                    "tail_to_zh": "游戏",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "manhunt run",
                    "tail_to_en": "manhunt run",
                    "tail_to_zh": "追捕",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "mins",
                    "tail_to_en": "mins",
                    "tail_to_zh": "分钟",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "s12",
                    "tail_to_en": "s12",
                    "tail_to_zh": "s12",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "loot",
                    "tail_to_en": "loot",
                    "tail_to_zh": "抢劫",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "rounds",
                    "tail_to_en": "rounds",
                    "tail_to_zh": "回合",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "change",
                    "tail_to_en": "change",
                    "tail_to_zh": "改变",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "keep",
                    "tail_to_en": "keep",
                    "tail_to_zh": "保持",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "nothing",
                    "tail_to_en": "nothing",
                    "tail_to_zh": "没有什么",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "sell",
                    "tail_to_en": "sell",
                    "tail_to_zh": "卖",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "team",
                    "tail_to_en": "team",
                    "tail_to_zh": "团队",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "receive",
                    "tail_to_en": "receive",
                    "tail_to_zh": "收到",
                    "count": 1
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "tail": "sks build tonight",
                    "tail_to_en": "sks build tonight",
                    "tail_to_zh": "sks 今晚建造",
                    "count": 1
                }
            ]
        }
    )


@app.route('/api/v1/portal/associated_second_word_comments', methods=['POST'])
def associated_second_word_comments():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": {
                "comments": [
                    {
                        "content": "Bro i dont think i have space for more then 2 🗿",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "i dont have a headphone for my pc",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Prolly gl4 at max just to make sure funni deaths dont ruin the dazzle xD",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Nah\nNo way its trash\nI mean cmon it look so good\nUnless u dont waste tons of money",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Irl they dont",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "It's ok if I dont like the fal",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "And you dont lose your mag this way",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "i dont know honestly",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Play it slow breh\nDont rush in\nOne of the most things that help me kill players is me hearing them first\nOnce you hear footsteps immediately crouch walk or slow walk that will reduce ur movement sound to green or yellow and just wait for them\nThats how i won most fights",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "we dont loot till kill all scavs",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "<@Mik> why you dont came back and grav my stuff",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I dont think u can jump like a bunny in tarkov and shot ppl",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "When i dont have gear i just get a backpack and do a naked run",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "why dont u use boxes?",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "I dont get to see my teamates getting head eyed",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Dont buy HK416",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "U dont have the right to talk to me",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "i dont even know where to put your id",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Dont worry it drops sometimes",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Nope the thermal has limited range. I dont use it",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "Just dont end up like the guys i kill",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "yes, if i dont need the attachments",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "So im in the health section rn and i dont see quickheal",
                        "content_to_en": "",
                        "content_to_zh": ""
                    }
                ],
                "sentiment_rating": [
                    {
                        "name": "negative",
                        "value": 1
                    },
                    {
                        "name": "neutral",
                        "value": 22
                    },
                    {
                        "name": "positive",
                        "value": 0
                    }
                ]
            }
        }
    )


@app.route('/api/v1/portal/associated_third_words', methods=['POST'])
def associated_third_words():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "have",
                    "three_to_en": "have",
                    "three_to_zh": "有",
                    "count": 10
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "use",
                    "three_to_en": "use",
                    "three_to_zh": "使用",
                    "count": 5
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "know",
                    "three_to_en": "know",
                    "three_to_zh": "知道",
                    "count": 4
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "think",
                    "three_to_en": "think",
                    "three_to_zh": "思考",
                    "count": 4
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "see",
                    "three_to_en": "see",
                    "three_to_zh": "看",
                    "count": 3
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "buy",
                    "three_to_en": "buy",
                    "three_to_zh": "买",
                    "count": 2
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "get",
                    "three_to_en": "get",
                    "three_to_zh": "得到",
                    "count": 2
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "hk416",
                    "three_to_en": "hk416",
                    "three_to_zh": "HK416",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "forgor",
                    "three_to_en": "forgor",
                    "three_to_zh": "放弃",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "rush",
                    "three_to_en": "rush",
                    "three_to_zh": "匆忙",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "kill",
                    "three_to_en": "kill",
                    "three_to_zh": "杀",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "end",
                    "three_to_en": "end",
                    "three_to_zh": "结尾",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "loot",
                    "three_to_en": "loot",
                    "three_to_zh": "抢劫",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "smokes",
                    "three_to_en": "smokes",
                    "three_to_zh": "抽烟",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "need",
                    "three_to_en": "need",
                    "three_to_zh": "需要",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "anything",
                    "three_to_en": "anything",
                    "three_to_zh": "任何事物",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "tons",
                    "three_to_en": "tons",
                    "three_to_zh": "吨",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "boxes",
                    "three_to_en": "boxes",
                    "three_to_zh": "盒子",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "worry",
                    "three_to_en": "worry",
                    "three_to_zh": "担心",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "mic",
                    "three_to_en": "mic",
                    "three_to_zh": "麦克风",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "like",
                    "three_to_en": "like",
                    "three_to_zh": "喜欢",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "gift system",
                    "three_to_en": "gift system",
                    "three_to_zh": "礼物系统",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "fr",
                    "three_to_en": "fr",
                    "three_to_zh": "fr",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "disgusting",
                    "three_to_en": "disgusting",
                    "three_to_zh": "恶心",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "waste",
                    "three_to_en": "waste",
                    "three_to_zh": "浪费",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "gear",
                    "three_to_en": "gear",
                    "three_to_zh": "齿轮",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "bag",
                    "three_to_en": "bag",
                    "three_to_zh": "包",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "confident",
                    "three_to_en": "confident",
                    "three_to_zh": "自信的",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "ruin",
                    "three_to_en": "ruin",
                    "three_to_zh": "废墟",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "quickheal",
                    "three_to_en": "quickheal",
                    "three_to_zh": "速愈",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "mag",
                    "three_to_en": "mag",
                    "three_to_zh": "杂志",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "gtranlsate",
                    "three_to_en": "gtranlsate",
                    "three_to_zh": "谷氨酸盐",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "dazzle",
                    "three_to_en": "dazzle",
                    "three_to_zh": "炫",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "fal",
                    "three_to_en": "fal",
                    "three_to_zh": "错误",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "play",
                    "three_to_en": "play",
                    "three_to_zh": "玩",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "headphone",
                    "three_to_en": "headphone",
                    "three_to_zh": "耳机",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "accuse",
                    "three_to_en": "accuse",
                    "three_to_zh": "告",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "right",
                    "three_to_en": "right",
                    "three_to_zh": "正确的",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "speak",
                    "three_to_en": "speak",
                    "three_to_zh": "说话",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "attachments",
                    "three_to_en": "attachments",
                    "three_to_zh": "附件",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "lose",
                    "three_to_en": "lose",
                    "three_to_zh": "失去",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "ab lite",
                    "three_to_en": "ab lite",
                    "three_to_zh": "精简版",
                    "count": 1
                },
                {
                    "one": "do",
                    "one_to_en": "do",
                    "one_to_zh": "做",
                    "two": "nt",
                    "two_to_en": "do",
                    "two_to_zh": "做",
                    "three": "bandange",
                    "three_to_en": "bandange",
                    "three_to_zh": "绷带",
                    "count": 1
                }
            ]
        }
    )


@app.route('/api/v1/portal/associated_third_word_comments', methods=['POST'])
def associated_third_word_comments():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": {
                "comments": [
                    {
                        "content": "Bro i dont think i have space for more then 2 🗿",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "i dont have a headphone for my pc",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "When i dont have gear i just get a backpack and do a naked run",
                        "content_to_en": "",
                        "content_to_zh": ""
                    },
                    {
                        "content": "U dont have the right to talk to me",
                        "content_to_en": "",
                        "content_to_zh": ""
                    }
                ],
                "sentiment_rating": [

                ]
            }
        }
    )


@app.route('/api/v1/portal/associated_statistic_first_words', methods=['POST'])
def associated_statistic_first_words():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "head": "use",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 68,
                    "rank": 1,
                    "rank_change":-179,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": False
                },
                {
                    "head": "need",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 55,
                    "rank": 2,
                    "rank_change": 0,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": True
                },
                {
                    "head": "good",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 54,
                    "rank": 3,
                    "rank_change": 0,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": True
                },
                {
                    "head": "armory",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 42,
                    "rank": 4,
                    "rank_change":-270,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": False
                },
                {
                    "head": "time",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 36,
                    "rank": 5,
                    "rank_change": 0,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": True
                },
                {
                    "head": "i",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 34,
                    "rank": 6,
                    "rank_change":-6,
                    "sentiment_rating": [
                        0,
                        1,
                        1
                    ],
                    "is_new": False
                },
                {
                    "head": "think",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 32,
                    "rank": 7,
                    "rank_change":-202,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": False
                },
                {
                    "head": "kill",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 30,
                    "rank": 8,
                    "rank_change": 0,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": False
                },
                {
                    "head": "full",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 29,
                    "rank": 9,
                    "rank_change":-3205,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "is_new": False
                },
                {
                    "head": "same",
                    "head_to_en": "",
                    "head_to_zh": "",
                    "count": 29,
                    "rank": 10,
                    "rank_change":-2538,
                    "sentiment_rating": [
                        0,
                        1,
                        1
                    ],
                    "is_new": False
                }
            ]
        }
    )


@app.route('/api/v1/portal/associated_statistic_second_words', methods=['POST'])
def associated_statistic_second_words():
    print(flask.request.json)
    with open('associated_statistic_second_words.json', 'r', encoding='utf8') as f:
        content = json.load(f)
    return flask.jsonify(content)


@app.route('/api/v1/portal/associated_statistic_third_words', methods=['POST'])
def associated_statistic_third_words():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "second": "nt",
                    "second_to_en": "nt",
                    "second_to_zh": "新台币",
                    "count": 4,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "correlation_degree": 10.181627,
                    "third": "think",
                    "third_to_en": "think",
                    "third_to_zh": "思考"
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "second": "nt",
                    "second_to_en": "nt",
                    "second_to_zh": "新台币",
                    "count": 4,
                    "sentiment_rating": [
                        1,
                        1,
                        0
                    ],
                    "correlation_degree": 7.2774615,
                    "third": "use",
                    "third_to_en": "use",
                    "third_to_zh": "使用"
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "second": "nt",
                    "second_to_en": "nt",
                    "second_to_zh": "新台币",
                    "count": 3,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "correlation_degree": 9.622011,
                    "third": "know",
                    "third_to_en": "know",
                    "third_to_zh": "知道"
                },
                {
                    "head": "hours",
                    "head_to_en": "hours",
                    "head_to_zh": "小时",
                    "second": "guys",
                    "second_to_en": "guys",
                    "second_to_zh": "伙计们",
                    "count": 2,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "correlation_degree": 12.08934,
                    "third": "have",
                    "third_to_en": "have",
                    "third_to_zh": "有"
                },
                {
                    "head": "ad",
                    "head_to_en": "ad",
                    "head_to_zh": "广告",
                    "second": "shiny",
                    "second_to_en": "shiny",
                    "second_to_zh": "闪亮的",
                    "count": 2,
                    "sentiment_rating": [
                        0,
                        2,
                        0
                    ],
                    "correlation_degree": 20.07678,
                    "third": "lgsg gercep wkw",
                    "third_to_en": "lgsg gercep wkw",
                    "third_to_zh": "lgsg gercep wkw"
                },
                {
                    "head": "yg",
                    "head_to_en": "yg",
                    "head_to_zh": "yg",
                    "second": "shiny",
                    "second_to_en": "shiny",
                    "second_to_zh": "闪亮的",
                    "count": 2,
                    "sentiment_rating": [
                        0,
                        2,
                        0
                    ],
                    "correlation_degree": 20.07678,
                    "third": "lgsg gercep wkw",
                    "third_to_en": "lgsg gercep wkw",
                    "third_to_zh": "lgsg gercep wkw"
                },
                {
                    "head": "do",
                    "head_to_en": "do",
                    "head_to_zh": "做",
                    "second": "guys",
                    "second_to_en": "guys",
                    "second_to_zh": "伙计们",
                    "count": 2,
                    "sentiment_rating": [
                        0,
                        1,
                        0
                    ],
                    "correlation_degree": 8.34692,
                    "third": "have",
                    "third_to_en": "have",
                    "third_to_zh": "有"
                },
                {
                    "head": "ad",
                    "head_to_en": "ad",
                    "head_to_zh": "广告",
                    "second": "shiny",
                    "second_to_en": "shiny",
                    "second_to_zh": "闪亮的",
                    "count": 2,
                    "sentiment_rating": [
                        0,
                        2,
                        0
                    ],
                    "correlation_degree": 20.07678,
                    "third": "shiny",
                    "third_to_en": "shiny",
                    "third_to_zh": "闪亮的"
                },
                {
                    "head": "galaxy s4",
                    "head_to_en": "galaxy s4",
                    "head_to_zh": "银河 s4",
                    "second": "long",
                    "second_to_en": "long",
                    "second_to_zh": "长的",
                    "count": 2,
                    "sentiment_rating": [
                        0,
                        2,
                        0
                    ],
                    "correlation_degree": 14.302228,
                    "third": "time",
                    "third_to_en": "time",
                    "third_to_zh": "时间"
                },
                {
                    "head": "bag",
                    "head_to_en": "bag",
                    "head_to_zh": "包",
                    "second": "movement",
                    "second_to_en": "movement",
                    "second_to_zh": "移动",
                    "count": 2,
                    "sentiment_rating": [
                        0,
                        2,
                        0
                    ],
                    "correlation_degree": 14.788513,
                    "third": "hard",
                    "third_to_en": "hard",
                    "third_to_zh": "难的"
                }
            ]
        }
    )


@app.route('/api/v1/portal/associated_graph', methods=['POST'])
def associated_graph():
    print(flask.request.json)
    with open('associated_graph.json', 'r', encoding='utf8') as f:
        content = json.load(f)
    return flask.jsonify(content)
    # return flask.jsonify({
    #     "ret_code": "0",
    #     "message": "Success",
    #     "data": []
    # })


@app.route('/api/v1/portal/associated_games', methods=['GET'])
def associated_games():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "Success",
        "data": [
            {
                "label": "UAMO",
                "value": "u10000000022"
            },
            {
                "label": "Nightgale",
                "value": "u11000000297"
            },
            {
                "label": "PUBG",
                "value": "ufc454d9b1af70b40588e2a6fa4da4a8b"
            }
        ]
    })


@app.route('/api/v1/portal/assistants_like_status', methods=['POST'])
def assistants_like_status():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": {
                "dislike": 1,
                "id": 2,
                "like": 1
            }
        }
    )


@app.route('/api/v1/portal/assistants_like', methods=['POST'])
def assistants_like():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success"
        }
    )


@app.route('/api/v1/portal/assistants_dislike', methods=['POST'])
def assistants_dislike():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success"
        }
    )


@app.route('/api/v1/portal/img2img', methods=['POST'])
def img2img():
    print(flask.request.files)
    print(flask.request.form)
    print(flask.request.json)
    time.sleep(11)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "success",
            "data": {
                # "raw_file_url": "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/aidraw/test/1.jpeg",
                "raw_file_url": "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/stable_diffusion/img2img/20230526060112-ori.jpg",
                "to_image_url": [
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/stable_diffusion/img2img/20230529154214-result0.png",
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/stable_diffusion/img2img/20230529154214-result1.png",
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/stable_diffusion/img2img/20230529154214-result2.png",
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/stable_diffusion/img2img/20230529154214-result3.png"
                ]
            }
        }
    )


@app.route('/api/v1/portal/gpt/minute', methods=['POST'])
def minute():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:06",
                    "count": 14
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:23",
                    "count": 11
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:05",
                    "count": 16
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:04",
                    "count": 4
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:33",
                    "count": 24
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:07",
                    "count": 6
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:30",
                    "count": 17
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:17",
                    "count": 11
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:10",
                    "count": 12
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:27",
                    "count": 7
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:21",
                    "count": 3
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:22",
                    "count": 21
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:15",
                    "count": 13
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:32",
                    "count": 14
                },
                {
                    "model": "gpt-4-32k",
                    "transform_time": "2023-06-29 09:17",
                    "count": 2
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:09",
                    "count": 9
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:26",
                    "count": 21
                },
                {
                    "model": "gpt-4-32k",
                    "transform_time": "2023-06-29 09:16",
                    "count": 4
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:18",
                    "count": 2
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:11",
                    "count": 5
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:28",
                    "count": 11
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:13",
                    "count": 19
                },
                {
                    "model": "gpt-4-32k",
                    "transform_time": "2023-06-29 09:27",
                    "count": 7
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:34",
                    "count": 16
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:24",
                    "count": 5
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:12",
                    "count": 7
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:16",
                    "count": 13
                },
                {
                    "model": "gpt-4-32k",
                    "transform_time": "2023-06-29 09:28",
                    "count": 1
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:19",
                    "count": 13
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:14",
                    "count": 13
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29 09:31",
                    "count": 12
                }
            ]
        }
    )


@app.route('/api/v1/portal/gpt/day', methods=['POST'])
def day():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data": [
                {
                    "model": "gpt-3.5-turbo",
                    "transform_time": "2023-06-28",
                    "count": 212
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-28",
                    "count": 1803
                },
                {
                    "model": "gpt-4",
                    "transform_time": "2023-06-29",
                    "count": 985
                },
                {
                    "model": "gpt-4-32k",
                    "transform_time": "2023-06-28",
                    "count": 920
                },
                {
                    "model": "gpt-4-32k",
                    "transform_time": "2023-06-29",
                    "count": 18
                },
                {
                    "model": "",
                    "transform_time": "2023-06-22",
                    "count": 70
                },
                {
                    "model": "",
                    "transform_time": "2023-06-23",
                    "count": 616
                },
                {
                    "model": "",
                    "transform_time": "2023-06-25",
                    "count": 229
                },
                {
                    "model": "",
                    "transform_time": "2023-06-26",
                    "count": 420
                },
                {
                    "model": "",
                    "transform_time": "2023-06-27",
                    "count": 445
                },
                {
                    "model": "",
                    "transform_time": "2023-06-28",
                    "count": 18
                }
            ]
        }
    )


@app.route('/api/v1/portal/source_audio', methods=['POST'])
def source_audio():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/stable_diffusion/source_audio/20230801033730-result0.mp3"
        }
    )


@app.route('/api/v1/portal/translation/query', methods=['POST'])
def query():
    print(flask.request.json)
    return flask.jsonify(
        {
            "ret_code": "0",
            "message": "Success",
            "data":[
                {
                    "task_id":1,
                    "task_name":"二次元-CON-cn-en",
                    "status":"init",
                    "category":"二次元",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"openai",
                    "embedding_service":"COS",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":2,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"二次元",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"azure",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":3,
                    "task_name":"二次元-CON-cn-en",
                    "status":"failed",
                    "category":"二次元",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"panic(err)",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":4,
                    "task_name":"二次元-CON-cn-en",
                    "status":"init",
                    "category":"射击",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":5,
                    "task_name":"二次元-CON-cn-en",
                    "status":"init",
                    "category":"二次元",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":6,
                    "task_name":"二次元-CON-cn-en",
                    "status":"init",
                    "category":"MOBA",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":7,
                    "task_name":"二次元-CON-cn-en",
                    "status":"init",
                    "category":"MMO",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":8,
                    "task_name":"二次元-CON-cn-en",
                    "status":"init",
                    "category":"Other",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":9,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"AVA",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":10,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"CON",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":11,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"COS",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":12,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"SOP",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":13,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"AUR",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":14,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"HTT",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":15,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"NKE",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":16,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"Re0",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":17,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"AOV",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":18,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"HOK",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":19,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"DN2",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":20,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"TDM",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":21,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"NBA",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":22,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"STF",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        },
        {       
                    "task_id":23,
                    "task_name":"二次元-CON-cn-en",
                    "status":"runing",
                    "category":"Other",
                    "game":"ROB",
                    "srclang":"cn",
                    "tolang":"en",
                    "embedding_type":"palm2",
                    "embedding_service":"pgvector",
                    "file_cos_url":"https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/portal/translation_training/20230823023921_tump_57s.svc",
                    "err_msg":"",
                    "update_time":"2023-08-23T19:52:00+08:00",
                    "create_time":"2023-08-23T19:52:00+08:00"
        }
]
        }
    )


@app.route('/api/v1/portal/translation/add', methods=['POST'])
def taskAdd():
    print(flask.request.form)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
         "task_id": 110
            
    })


@app.route('/api/v1/portal/operate_data', methods=['POST'])
def operateData():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        
    "portal":[
        {
            "pv":12.156,
            "uv":40.12358
        },
        {
            "pv":10.2568,
            "uv":140.12749
        }
    ],
    "gpt_proxy":[
        {
            "pv":0.12,
            "uv":0.3689
        },
        {
            "pv":0.87456,
            "uv":0.156
        }
    ],
    "bot": {
        "current": {
            "list": [
                {
                    "chat_ource": "slackbot",
                    "pv": 686,
                    "uv": 10
                },
                {
                    "chat_ource": "web",
                    "pv": 594,
                    "uv": 16
                },
                {
                    "chat_ource": "webot",
                    "pv": 592,
                    "uv": 10
                }
            ]
        },
        "year": {
            "list": [
                {
                    "chat_ource": "slackbot",
                    "pv": 686,
                    "uv": 10
                },
                {
                    "chat_ource": "web",
                    "pv": 594,
                    "uv": 16
                },
                {
                    "chat_ource": "webot",
                    "pv": 592,
                    "uv": 10
                }
            ]
        }
    },
    "mlflow_info":{
        "servers_count":1235,
        "cpu_usage_rate":'50%',
        "memery_usage_rate":'60%'
    },
    "gpt_detail":[
        {
            "err_code":200,
            "count":10
        },
        {
            "err_code":400,
            "count":10
        }
    ]
    })


@app.route('/api/v1/portal/automation/subscribe', methods=['POST'])
def subscribe():
    print(flask.request.json)
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
    })

    
@app.route('/api/v1/portal/summary_modify_history', methods=['GET'])
def SummaryHistory():
    return flask.jsonify({
        "ret_code": "0",
        "message": "success",
        "data":[
        {
            "cluster_id": "d665fbf9ad26c37ff36f6144df29709d",
            "table_type_name": "",
            "before_value": "{\"id\":9715,\"unified_id\":\"ufc454d9b1af70b40588e2a6fa4da4a8b\",\"edition_id\":\"\",\"event_id\":\"0ec26272dbd55f4e6e70389b72d3075d\",\"cluster_id\":\"d665fbf9ad26c37ff36f6144df29709d\",\"event_gpt_content\":\"在比赛中，有玩家为自己的朋友开脱，有人需要有钱的朋友，有人想要朋友，还有人在讨论比赛的难度和预测胜负。\",\"channel_type\":\"total\",\"data_sentiment\":\"total\",\"data_language\":\"all\",\"language_distribution\":\"{\\\"it\\\": [1, 0.53], \\\"eo\\\": [2, 1.06], \\\"ar\\\": [45, 23.94], \\\"hu\\\": [1, 0.53], \\\"mt\\\": [1, 0.53], \\\"sh\\\": [1, 0.53], \\\"en\\\": [118, 62.77], \\\"no\\\": [1, 0.53], \\\"id\\\": [1, 0.53], \\\"ja\\\": [2, 1.06], \\\"pt\\\": [2, 1.06], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"fr\\\": [1, 0.53], \\\"br\\\": [1, 0.53], \\\"sw\\\": [2, 1.06]}\",\"market_distribution\":\"{\\\"it\\\": [2, 1.06], \\\"in\\\": [30, 15.96], \\\"sa\\\": [47, 25.0], \\\"global\\\": [96, 51.06], \\\"pk\\\": [1, 0.53], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"de\\\": [1, 0.53], \\\"us\\\": [2, 1.06]}\",\"keywords\":\"friend:34:3.0|match:12:3.0|صديقي:5:3.0|arkadaşlar:5:3.0|friend request:4:3.0|september 3:4:3.0|3 match:4:3.0|صاحبي:3:3.0|وإي:3:3.0|لدي لغبمحقق:3:3.0|حل المشكلة وشكرا:3:3.0|ملاحظة:3:3.0|لعبةرائعة:3:3.0|rich friend:3:3.0|نقيب:3:3.0|جدا ومستوناقليل:3:3.0|اصحابي:3:3.0|ضد اشخاصمحترفين:3:3.0|doge:3:3.0|الهكات:3:3.0|bhej:2:3.0|winordie tournament:2:3.0|1000 registration:2:3.0|aktif:2:3.0|صديقه:2:3.0|pubgmobile:2:3.0|1 »:2:3.0|tournament prize:2:3.0|matches:2:3.0|اصدقاء:2:3.0|صاحب:2:3.0|match 2:2:3.0|s1:2:3.0|information:2:3.0|التوب:2:3.0|online:2:3.0|now open:2:3.0|maç:2:3.0|kappa:2:3.0|المهم:2:3.0|buy the slot:2:3.0|english:2:3.0|paid one:2:3.0|الله:1:3.0|prize match:1:3.0|have friends:1:3.0|20 cet:1:3.0|rha:1:3.0|شوي:1:3.0|eshu:1:3.0|body shaming:1:3.0|bar opponents:1:3.0|ملاكمه:1:3.0|brotha:1:3.0|1225 uc:1:3.0|even check:1:3.0|pass:1:3.0|1225uc prizepool:1:3.0|تمام يصديقى:1:3.0|ammer friend:1:3.0|over30と一緒:1:3.0|روم:1:3.0|شباب:1:3.0|1 point:1:3.0|资深挂壁:1:3.0|çöktü:1:3.0|weekly match:1:3.0|crew challenge yerinde:1:3.0|solo:1:3.0|most trustworthy friend:1:3.0|back bitting:1:3.0|hypocryte:1:3.0|بيت صاحبي:1:3.0|مع نفس:1:3.0|王者外挂:1:3.0|boy or girl:1:3.0|和平辅助:1:3.0|room match:1:3.0|chinese pubg mobile:1:3.0|need friends:1:3.0|kya:1:3.0|believe india:1:3.0|show a friend:1:3.0|already matching:1:3.0|mission:1:3.0|club prize:1:3.0|igl fragger:1:3.0|bohot matches:1:3.0|和平精英:1:3.0|2 nepal:1:3.0|mod:1:3.0|more matches:1:3.0|die:1:3.0|best test:1:3.0|overthinking:1:3.0|4 matches:1:3.0|milega:1:3.0|pool tournament:1:3.0|10 - 20 mins average:1:3.0|اصدقائي والعب:1:3.0\",\"avg_sentiment\":\"3\",\"sentiment_rating\":3,\"count\":186,\"comment_uins\":\"\",\"start_time\":\"2023-09-03 00:00:00\",\"end_time\":\"2023-09-04 00:00:00\",\"md5_uin\":\"d6d6aca7863942e208be1ecdd810e31a\",\"cluster_type\":\"summary\",\"hint_tag\":\"0\",\"days\":1,\"rank\":1,\"new_icon\":0,\"hot_icon\":1,\"rise_icon\":0,\"insert_time\":\"2023-10-07T16:47:01Z\",\"isvalid\":1}",
            "after_value": "{\"id\":9715,\"unified_id\":\"ufc454d9b1af70b40588e2a6fa4da4a8b\",\"edition_id\":\"\",\"event_id\":\"0ec26272dbd55f4e6e70389b72d3075d\",\"cluster_id\":\"d665fbf9ad26c37ff36f6144df29709d\",\"event_gpt_content\":\"在比赛中，有玩家为自己的朋友开脱，有人需要有钱的朋友，有人想要朋友，还有人在讨论比赛的难度和预测胜负。\",\"channel_type\":\"total\",\"data_sentiment\":\"total\",\"data_language\":\"all\",\"language_distribution\":\"{\\\"it\\\": [1, 0.53], \\\"eo\\\": [2, 1.06], \\\"ar\\\": [45, 23.94], \\\"hu\\\": [1, 0.53], \\\"mt\\\": [1, 0.53], \\\"sh\\\": [1, 0.53], \\\"en\\\": [118, 62.77], \\\"no\\\": [1, 0.53], \\\"id\\\": [1, 0.53], \\\"ja\\\": [2, 1.06], \\\"pt\\\": [2, 1.06], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"fr\\\": [1, 0.53], \\\"br\\\": [1, 0.53], \\\"sw\\\": [2, 1.06]}\",\"market_distribution\":\"{\\\"it\\\": [2, 1.06], \\\"in\\\": [30, 15.96], \\\"sa\\\": [47, 25.0], \\\"global\\\": [96, 51.06], \\\"pk\\\": [1, 0.53], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"de\\\": [1, 0.53], \\\"us\\\": [2, 1.06]}\",\"keywords\":\"friend:34:3.0|match:12:3.0|صديقي:5:3.0|arkadaşlar:5:3.0|friend request:4:3.0|september 3:4:3.0|3 match:4:3.0|صاحبي:3:3.0|وإي:3:3.0|لدي لغبمحقق:3:3.0|حل المشكلة وشكرا:3:3.0|ملاحظة:3:3.0|لعبةرائعة:3:3.0|rich friend:3:3.0|نقيب:3:3.0|جدا ومستوناقليل:3:3.0|اصحابي:3:3.0|ضد اشخاصمحترفين:3:3.0|doge:3:3.0|الهكات:3:3.0|bhej:2:3.0|winordie tournament:2:3.0|1000 registration:2:3.0|aktif:2:3.0|صديقه:2:3.0|pubgmobile:2:3.0|1 »:2:3.0|tournament prize:2:3.0|matches:2:3.0|اصدقاء:2:3.0|صاحب:2:3.0|match 2:2:3.0|s1:2:3.0|information:2:3.0|التوب:2:3.0|online:2:3.0|now open:2:3.0|maç:2:3.0|kappa:2:3.0|المهم:2:3.0|buy the slot:2:3.0|english:2:3.0|paid one:2:3.0|الله:1:3.0|prize match:1:3.0|have friends:1:3.0|20 cet:1:3.0|rha:1:3.0|شوي:1:3.0|eshu:1:3.0|body shaming:1:3.0|bar opponents:1:3.0|ملاكمه:1:3.0|brotha:1:3.0|1225 uc:1:3.0|even check:1:3.0|pass:1:3.0|1225uc prizepool:1:3.0|تمام يصديقى:1:3.0|ammer friend:1:3.0|over30と一緒:1:3.0|روم:1:3.0|شباب:1:3.0|1 point:1:3.0|资深挂壁:1:3.0|çöktü:1:3.0|weekly match:1:3.0|crew challenge yerinde:1:3.0|solo:1:3.0|most trustworthy friend:1:3.0|back bitting:1:3.0|hypocryte:1:3.0|بيت صاحبي:1:3.0|مع نفس:1:3.0|王者外挂:1:3.0|boy or girl:1:3.0|和平辅助:1:3.0|room match:1:3.0|chinese pubg mobile:1:3.0|need friends:1:3.0|kya:1:3.0|believe india:1:3.0|show a friend:1:3.0|already matching:1:3.0|mission:1:3.0|club prize:1:3.0|igl fragger:1:3.0|bohot matches:1:3.0|和平精英:1:3.0|2 nepal:1:3.0|mod:1:3.0|more matches:1:3.0|die:1:3.0|best test:1:3.0|overthinking:1:3.0|4 matches:1:3.0|milega:1:3.0|pool tournament:1:3.0|10 - 20 mins average:1:3.0|اصدقائي والعب:1:3.0\",\"avg_sentiment\":\"3\",\"sentiment_rating\":3,\"count\":186,\"comment_uins\":\"\",\"start_time\":\"2023-09-03 00:00:00\",\"end_time\":\"2023-09-04 00:00:00\",\"md5_uin\":\"d6d6aca7863942e208be1ecdd810e31a\",\"cluster_type\":\"summary\",\"hint_tag\":\"0\",\"days\":1,\"rank\":1,\"new_icon\":0,\"hot_icon\":1,\"rise_icon\":0,\"insert_time\":\"2023-10-08 17:57:13\",\"isvalid\":1}",
            "insert_time": "2023-10-08 09:57:13",
            "creator": "gc_wangyingwen"
        },
        {
            "cluster_id": "d665fbf9ad26c37ff36f6144df29709d",
            "table_type_name": "",
            "before_value": "{\"id\":9715,\"unified_id\":\"ufc454d9b1af70b40588e2a6fa4da4a8b\",\"edition_id\":\"\",\"event_id\":\"0ec26272dbd55f4e6e70389b72d3075d\",\"cluster_id\":\"d665fbf9ad26c37ff36f6144df29709d\",\"event_gpt_content\":\"在比赛中，有玩家为自己的朋友开脱，有人需要有钱的朋友，有人想要朋友，还有人在讨论比赛的难度和预测胜负。\",\"channel_type\":\"total\",\"data_sentiment\":\"total\",\"data_language\":\"all\",\"language_distribution\":\"{\\\"it\\\": [1, 0.53], \\\"eo\\\": [2, 1.06], \\\"ar\\\": [45, 23.94], \\\"hu\\\": [1, 0.53], \\\"mt\\\": [1, 0.53], \\\"sh\\\": [1, 0.53], \\\"en\\\": [118, 62.77], \\\"no\\\": [1, 0.53], \\\"id\\\": [1, 0.53], \\\"ja\\\": [2, 1.06], \\\"pt\\\": [2, 1.06], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"fr\\\": [1, 0.53], \\\"br\\\": [1, 0.53], \\\"sw\\\": [2, 1.06]}\",\"market_distribution\":\"{\\\"it\\\": [2, 1.06], \\\"in\\\": [30, 15.96], \\\"sa\\\": [47, 25.0], \\\"global\\\": [96, 51.06], \\\"pk\\\": [1, 0.53], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"de\\\": [1, 0.53], \\\"us\\\": [2, 1.06]}\",\"keywords\":\"friend:34:3.0|match:12:3.0|صديقي:5:3.0|arkadaşlar:5:3.0|friend request:4:3.0|september 3:4:3.0|3 match:4:3.0|صاحبي:3:3.0|وإي:3:3.0|لدي لغبمحقق:3:3.0|حل المشكلة وشكرا:3:3.0|ملاحظة:3:3.0|لعبةرائعة:3:3.0|rich friend:3:3.0|نقيب:3:3.0|جدا ومستوناقليل:3:3.0|اصحابي:3:3.0|ضد اشخاصمحترفين:3:3.0|doge:3:3.0|الهكات:3:3.0|bhej:2:3.0|winordie tournament:2:3.0|1000 registration:2:3.0|aktif:2:3.0|صديقه:2:3.0|pubgmobile:2:3.0|1 »:2:3.0|tournament prize:2:3.0|matches:2:3.0|اصدقاء:2:3.0|صاحب:2:3.0|match 2:2:3.0|s1:2:3.0|information:2:3.0|التوب:2:3.0|online:2:3.0|now open:2:3.0|maç:2:3.0|kappa:2:3.0|المهم:2:3.0|buy the slot:2:3.0|english:2:3.0|paid one:2:3.0|الله:1:3.0|prize match:1:3.0|have friends:1:3.0|20 cet:1:3.0|rha:1:3.0|شوي:1:3.0|eshu:1:3.0|body shaming:1:3.0|bar opponents:1:3.0|ملاكمه:1:3.0|brotha:1:3.0|1225 uc:1:3.0|even check:1:3.0|pass:1:3.0|1225uc prizepool:1:3.0|تمام يصديقى:1:3.0|ammer friend:1:3.0|over30と一緒:1:3.0|روم:1:3.0|شباب:1:3.0|1 point:1:3.0|资深挂壁:1:3.0|çöktü:1:3.0|weekly match:1:3.0|crew challenge yerinde:1:3.0|solo:1:3.0|most trustworthy friend:1:3.0|back bitting:1:3.0|hypocryte:1:3.0|بيت صاحبي:1:3.0|مع نفس:1:3.0|王者外挂:1:3.0|boy or girl:1:3.0|和平辅助:1:3.0|room match:1:3.0|chinese pubg mobile:1:3.0|need friends:1:3.0|kya:1:3.0|believe india:1:3.0|show a friend:1:3.0|already matching:1:3.0|mission:1:3.0|club prize:1:3.0|igl fragger:1:3.0|bohot matches:1:3.0|和平精英:1:3.0|2 nepal:1:3.0|mod:1:3.0|more matches:1:3.0|die:1:3.0|best test:1:3.0|overthinking:1:3.0|4 matches:1:3.0|milega:1:3.0|pool tournament:1:3.0|10 - 20 mins average:1:3.0|اصدقائي والعب:1:3.0\",\"avg_sentiment\":\"3\",\"sentiment_rating\":3,\"count\":186,\"comment_uins\":\"\",\"start_time\":\"2023-09-03 00:00:00\",\"end_time\":\"2023-09-04 00:00:00\",\"md5_uin\":\"d6d6aca7863942e208be1ecdd810e31a\",\"cluster_type\":\"summary\",\"hint_tag\":\"0\",\"days\":1,\"rank\":1,\"new_icon\":0,\"hot_icon\":1,\"rise_icon\":0,\"insert_time\":\"2023-10-08T17:57:13Z\",\"isvalid\":1}",
            "after_value": "{\"id\":9715,\"unified_id\":\"ufc454d9b1af70b40588e2a6fa4da4a8b\",\"edition_id\":\"\",\"event_id\":\"0ec26272dbd55f4e6e70389b72d3075d\",\"cluster_id\":\"d665fbf9ad26c37ff36f6144df29709d\",\"event_gpt_content\":\"在比赛中，有玩家为自己的朋友开脱，有人需要有钱的朋友，有人想要朋友，还有人在讨论比赛的难度和预测胜负。\",\"channel_type\":\"total\",\"data_sentiment\":\"total\",\"data_language\":\"all\",\"language_distribution\":\"{\\\"it\\\": [1, 0.53], \\\"eo\\\": [2, 1.06], \\\"ar\\\": [45, 23.94], \\\"hu\\\": [1, 0.53], \\\"mt\\\": [1, 0.53], \\\"sh\\\": [1, 0.53], \\\"en\\\": [118, 62.77], \\\"no\\\": [1, 0.53], \\\"id\\\": [1, 0.53], \\\"ja\\\": [2, 1.06], \\\"pt\\\": [2, 1.06], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"fr\\\": [1, 0.53], \\\"br\\\": [1, 0.53], \\\"sw\\\": [2, 1.06]}\",\"market_distribution\":\"{\\\"it\\\": [2, 1.06], \\\"in\\\": [30, 15.96], \\\"sa\\\": [47, 25.0], \\\"global\\\": [96, 51.06], \\\"pk\\\": [1, 0.53], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"de\\\": [1, 0.53], \\\"us\\\": [2, 1.06]}\",\"keywords\":\"friend:34:3.0|match:12:3.0|صديقي:5:3.0|arkadaşlar:5:3.0|friend request:4:3.0|september 3:4:3.0|3 match:4:3.0|صاحبي:3:3.0|وإي:3:3.0|لدي لغبمحقق:3:3.0|حل المشكلة وشكرا:3:3.0|ملاحظة:3:3.0|لعبةرائعة:3:3.0|rich friend:3:3.0|نقيب:3:3.0|جدا ومستوناقليل:3:3.0|اصحابي:3:3.0|ضد اشخاصمحترفين:3:3.0|doge:3:3.0|الهكات:3:3.0|bhej:2:3.0|winordie tournament:2:3.0|1000 registration:2:3.0|aktif:2:3.0|صديقه:2:3.0|pubgmobile:2:3.0|1 »:2:3.0|tournament prize:2:3.0|matches:2:3.0|اصدقاء:2:3.0|صاحب:2:3.0|match 2:2:3.0|s1:2:3.0|information:2:3.0|التوب:2:3.0|online:2:3.0|now open:2:3.0|maç:2:3.0|kappa:2:3.0|المهم:2:3.0|buy the slot:2:3.0|english:2:3.0|paid one:2:3.0|الله:1:3.0|prize match:1:3.0|have friends:1:3.0|20 cet:1:3.0|rha:1:3.0|شوي:1:3.0|eshu:1:3.0|body shaming:1:3.0|bar opponents:1:3.0|ملاكمه:1:3.0|brotha:1:3.0|1225 uc:1:3.0|even check:1:3.0|pass:1:3.0|1225uc prizepool:1:3.0|تمام يصديقى:1:3.0|ammer friend:1:3.0|over30と一緒:1:3.0|روم:1:3.0|شباب:1:3.0|1 point:1:3.0|资深挂壁:1:3.0|çöktü:1:3.0|weekly match:1:3.0|crew challenge yerinde:1:3.0|solo:1:3.0|most trustworthy friend:1:3.0|back bitting:1:3.0|hypocryte:1:3.0|بيت صاحبي:1:3.0|مع نفس:1:3.0|王者外挂:1:3.0|boy or girl:1:3.0|和平辅助:1:3.0|room match:1:3.0|chinese pubg mobile:1:3.0|need friends:1:3.0|kya:1:3.0|believe india:1:3.0|show a friend:1:3.0|already matching:1:3.0|mission:1:3.0|club prize:1:3.0|igl fragger:1:3.0|bohot matches:1:3.0|和平精英:1:3.0|2 nepal:1:3.0|mod:1:3.0|more matches:1:3.0|die:1:3.0|best test:1:3.0|overthinking:1:3.0|4 matches:1:3.0|milega:1:3.0|pool tournament:1:3.0|10 - 20 mins average:1:3.0|اصدقائي والعب:1:3.0\",\"avg_sentiment\":\"3\",\"sentiment_rating\":3,\"count\":186,\"comment_uins\":\"\",\"start_time\":\"2023-09-03 00:00:00\",\"end_time\":\"2023-09-04 00:00:00\",\"md5_uin\":\"d6d6aca7863942e208be1ecdd810e31a\",\"cluster_type\":\"summary\",\"hint_tag\":\"0\",\"days\":1,\"rank\":1,\"new_icon\":0,\"hot_icon\":1,\"rise_icon\":0,\"insert_time\":\"2023-10-08 17:57:40\",\"isvalid\":1}",
            "insert_time": "2023-10-08 09:57:40",
            "creator": "gc_wangyingwen"
        },
        {
            "cluster_id": "d665fbf9ad26c37ff36f6144df29709d",
            "table_type_name": "",
            "before_value": "{\"id\":9715,\"unified_id\":\"ufc454d9b1af70b40588e2a6fa4da4a8b\",\"edition_id\":\"\",\"event_id\":\"0ec26272dbd55f4e6e70389b72d3075d\",\"cluster_id\":\"d665fbf9ad26c37ff36f6144df29709d\",\"event_gpt_content\":\"在比赛中，有玩家为自己的朋友开脱，有人需要有钱的朋友，有人想要朋友，还有人在讨论比赛的难度和预测胜负。\",\"channel_type\":\"total\",\"data_sentiment\":\"total\",\"data_language\":\"all\",\"language_distribution\":\"{\\\"it\\\": [1, 0.53], \\\"eo\\\": [2, 1.06], \\\"ar\\\": [45, 23.94], \\\"hu\\\": [1, 0.53], \\\"mt\\\": [1, 0.53], \\\"sh\\\": [1, 0.53], \\\"en\\\": [118, 62.77], \\\"no\\\": [1, 0.53], \\\"id\\\": [1, 0.53], \\\"ja\\\": [2, 1.06], \\\"pt\\\": [2, 1.06], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"fr\\\": [1, 0.53], \\\"br\\\": [1, 0.53], \\\"sw\\\": [2, 1.06]}\",\"market_distribution\":\"{\\\"it\\\": [2, 1.06], \\\"in\\\": [30, 15.96], \\\"sa\\\": [47, 25.0], \\\"global\\\": [96, 51.06], \\\"pk\\\": [1, 0.53], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"de\\\": [1, 0.53], \\\"us\\\": [2, 1.06]}\",\"keywords\":\"friend:34:3.0|match:12:3.0|صديقي:5:3.0|arkadaşlar:5:3.0|friend request:4:3.0|september 3:4:3.0|3 match:4:3.0|صاحبي:3:3.0|وإي:3:3.0|لدي لغبمحقق:3:3.0|حل المشكلة وشكرا:3:3.0|ملاحظة:3:3.0|لعبةرائعة:3:3.0|rich friend:3:3.0|نقيب:3:3.0|جدا ومستوناقليل:3:3.0|اصحابي:3:3.0|ضد اشخاصمحترفين:3:3.0|doge:3:3.0|الهكات:3:3.0|bhej:2:3.0|winordie tournament:2:3.0|1000 registration:2:3.0|aktif:2:3.0|صديقه:2:3.0|pubgmobile:2:3.0|1 »:2:3.0|tournament prize:2:3.0|matches:2:3.0|اصدقاء:2:3.0|صاحب:2:3.0|match 2:2:3.0|s1:2:3.0|information:2:3.0|التوب:2:3.0|online:2:3.0|now open:2:3.0|maç:2:3.0|kappa:2:3.0|المهم:2:3.0|buy the slot:2:3.0|english:2:3.0|paid one:2:3.0|الله:1:3.0|prize match:1:3.0|have friends:1:3.0|20 cet:1:3.0|rha:1:3.0|شوي:1:3.0|eshu:1:3.0|body shaming:1:3.0|bar opponents:1:3.0|ملاكمه:1:3.0|brotha:1:3.0|1225 uc:1:3.0|even check:1:3.0|pass:1:3.0|1225uc prizepool:1:3.0|تمام يصديقى:1:3.0|ammer friend:1:3.0|over30と一緒:1:3.0|روم:1:3.0|شباب:1:3.0|1 point:1:3.0|资深挂壁:1:3.0|çöktü:1:3.0|weekly match:1:3.0|crew challenge yerinde:1:3.0|solo:1:3.0|most trustworthy friend:1:3.0|back bitting:1:3.0|hypocryte:1:3.0|بيت صاحبي:1:3.0|مع نفس:1:3.0|王者外挂:1:3.0|boy or girl:1:3.0|和平辅助:1:3.0|room match:1:3.0|chinese pubg mobile:1:3.0|need friends:1:3.0|kya:1:3.0|believe india:1:3.0|show a friend:1:3.0|already matching:1:3.0|mission:1:3.0|club prize:1:3.0|igl fragger:1:3.0|bohot matches:1:3.0|和平精英:1:3.0|2 nepal:1:3.0|mod:1:3.0|more matches:1:3.0|die:1:3.0|best test:1:3.0|overthinking:1:3.0|4 matches:1:3.0|milega:1:3.0|pool tournament:1:3.0|10 - 20 mins average:1:3.0|اصدقائي والعب:1:3.0\",\"avg_sentiment\":\"3\",\"sentiment_rating\":3,\"count\":186,\"comment_uins\":\"\",\"start_time\":\"2023-09-03 00:00:00\",\"end_time\":\"2023-09-04 00:00:00\",\"md5_uin\":\"d6d6aca7863942e208be1ecdd810e31a\",\"cluster_type\":\"summary\",\"hint_tag\":\"0\",\"days\":1,\"rank\":1,\"new_icon\":0,\"hot_icon\":1,\"rise_icon\":0,\"insert_time\":\"2023-10-08T17:57:40Z\",\"isvalid\":1}",
            "after_value": "{\"id\":9715,\"unified_id\":\"ufc454d9b1af70b40588e2a6fa4da4a8b\",\"edition_id\":\"\",\"event_id\":\"0ec26272dbd55f4e6e70389b72d3075d\",\"cluster_id\":\"d665fbf9ad26c37ff36f6144df29709d\",\"event_gpt_content\":\"在比赛中，有玩家为自己的朋友开脱，有人需要有钱的朋友，有人想要朋友，还有人在讨论比赛的难度和预测胜负。\",\"channel_type\":\"total\",\"data_sentiment\":\"total\",\"data_language\":\"all\",\"language_distribution\":\"{\\\"it\\\": [1, 0.53], \\\"eo\\\": [2, 1.06], \\\"ar\\\": [45, 23.94], \\\"hu\\\": [1, 0.53], \\\"mt\\\": [1, 0.53], \\\"sh\\\": [1, 0.53], \\\"en\\\": [118, 62.77], \\\"no\\\": [1, 0.53], \\\"id\\\": [1, 0.53], \\\"ja\\\": [2, 1.06], \\\"pt\\\": [2, 1.06], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"fr\\\": [1, 0.53], \\\"br\\\": [1, 0.53], \\\"sw\\\": [2, 1.06]}\",\"market_distribution\":\"{\\\"it\\\": [2, 1.06], \\\"in\\\": [30, 15.96], \\\"sa\\\": [47, 25.0], \\\"global\\\": [96, 51.06], \\\"pk\\\": [1, 0.53], \\\"tr\\\": [8, 4.26], \\\"uz\\\": [1, 0.53], \\\"de\\\": [1, 0.53], \\\"us\\\": [2, 1.06]}\",\"keywords\":\"friend:34:3.0|match:12:3.0|صديقي:5:3.0|arkadaşlar:5:3.0|friend request:4:3.0|september 3:4:3.0|3 match:4:3.0|صاحبي:3:3.0|وإي:3:3.0|لدي لغبمحقق:3:3.0|حل المشكلة وشكرا:3:3.0|ملاحظة:3:3.0|لعبةرائعة:3:3.0|rich friend:3:3.0|نقيب:3:3.0|جدا ومستوناقليل:3:3.0|اصحابي:3:3.0|ضد اشخاصمحترفين:3:3.0|doge:3:3.0|الهكات:3:3.0|bhej:2:3.0|winordie tournament:2:3.0|1000 registration:2:3.0|aktif:2:3.0|صديقه:2:3.0|pubgmobile:2:3.0|1 »:2:3.0|tournament prize:2:3.0|matches:2:3.0|اصدقاء:2:3.0|صاحب:2:3.0|match 2:2:3.0|s1:2:3.0|information:2:3.0|التوب:2:3.0|online:2:3.0|now open:2:3.0|maç:2:3.0|kappa:2:3.0|المهم:2:3.0|buy the slot:2:3.0|english:2:3.0|paid one:2:3.0|الله:1:3.0|prize match:1:3.0|have friends:1:3.0|20 cet:1:3.0|rha:1:3.0|شوي:1:3.0|eshu:1:3.0|body shaming:1:3.0|bar opponents:1:3.0|ملاكمه:1:3.0|brotha:1:3.0|1225 uc:1:3.0|even check:1:3.0|pass:1:3.0|1225uc prizepool:1:3.0|تمام يصديقى:1:3.0|ammer friend:1:3.0|over30と一緒:1:3.0|روم:1:3.0|شباب:1:3.0|1 point:1:3.0|资深挂壁:1:3.0|çöktü:1:3.0|weekly match:1:3.0|crew challenge yerinde:1:3.0|solo:1:3.0|most trustworthy friend:1:3.0|back bitting:1:3.0|hypocryte:1:3.0|بيت صاحبي:1:3.0|مع نفس:1:3.0|王者外挂:1:3.0|boy or girl:1:3.0|和平辅助:1:3.0|room match:1:3.0|chinese pubg mobile:1:3.0|need friends:1:3.0|kya:1:3.0|believe india:1:3.0|show a friend:1:3.0|already matching:1:3.0|mission:1:3.0|club prize:1:3.0|igl fragger:1:3.0|bohot matches:1:3.0|和平精英:1:3.0|2 nepal:1:3.0|mod:1:3.0|more matches:1:3.0|die:1:3.0|best test:1:3.0|overthinking:1:3.0|4 matches:1:3.0|milega:1:3.0|pool tournament:1:3.0|10 - 20 mins average:1:3.0|اصدقائي والعب:1:3.0\",\"avg_sentiment\":\"3\",\"sentiment_rating\":3,\"count\":186,\"comment_uins\":\"\",\"start_time\":\"2023-09-03 00:00:00\",\"end_time\":\"2023-09-04 00:00:00\",\"md5_uin\":\"d6d6aca7863942e208be1ecdd810e31a\",\"cluster_type\":\"summary\",\"hint_tag\":\"0\",\"days\":1,\"rank\":1,\"new_icon\":0,\"hot_icon\":1,\"rise_icon\":0,\"insert_time\":\"2023-10-09 09:43:40\",\"isvalid\":1}",
            "insert_time": "2023-10-09 01:43:40",
            "creator": "gc_wangyingwen"
        }
    ]
    })

    
@app.route('/api/v1/kelong/images', methods=['POST'])
def images():
    state = flask.request.args.get("state")
    return flask.jsonify({
        "ret_code":"0",
    "message":"success",
    "data":[
        {
            "create_time":"2023-08-02 00:00:00",
            "raw_file_id":1,
            "raw_file":"https://swiperjs.com/demos/images/nature-4.jpg",
            "to_image_list":[
                "https://swiperjs.com/demos/images/nature-3.jpg"

            ]
        }
    ]
    })


@app.route('/api/v1/kelong/banner_images', methods=['POST'])
def banner():
    return flask.jsonify({
    "ret_code": "0",
    "message": "success",
    "data": {
        "style_image_map": {
            "pubgm": {
                "banner_image_list": [
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/techweek/result_1698066908963436499_mason.jpg",
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/techweek/result_1698061043684412848_mason.jpg",
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/techweek/result_1698059426263585737_mason.jpg",
                    "https://ua-sg-1300342648.cos.ap-singapore.myqcloud.com/techweek/result_1698059246443983829_image.jpg"
                ]
            },
            "sop": {
                "banner_image_list": []
            }
        }
    }
})


@app.route('/api/v1/portal/get_task_list', methods=['POST'])
def user_get_task_list():
    param=flask.request.json
    game = param["game"]
    page_num = param["page_num"]
    page_size = param["page_size"]
    # if ( game is None ) or ( page_num is None)or( page_size is None):
    #     print('---------game',game)
    #     print('---------game',page_num)
    #     print('---------game',page_size)
    #     return flask.jsonify(
    #         {"ret_code": "-1","message": "game code 为空 or page_num=0 or page_size=0","data":{}}
    #     )
    return flask.jsonify(
               {
            "err_code": "0",
            "err_msg": "0",
            "task_list": [
                {
                    "task_id": "10",
                    "task_name": "okkk",
                    "game": "hok",
                    "state": 3,
                    "create_time": "1697703894",
                    "update_time": "1698218208",
                    "data_version": "15",
                    "creator": "xiaoming",
                    "analysze_sql": "SELECT * FROM test",
                    "extract_sql": "SELECT * FROM test",
                    "output": "",
                    "analysis_result": "{\"game_code\":\"hok\",\"source\":\"test\",\"labels\":[\"id\",\"email\",\"company\"],\"operation\":[{\"tag_name\":\"id\",\"tag_comment\":\"Email\",\"logicType\":\"\",\"inputValue\":\"1\",\"opType\":1,\"tag_id\":\"25\",\"ck_source\":\"\",\"thive_source\":\"\",\"label_valid\":0,\"calc_valid\":0,\"tag_express_option\":\"\",\"tag_express_value\":\"\"},{\"tag_name\":\"email\",\"tag_comment\":\"Email\",\"logicType\":1,\"inputValue\":\"2\",\"opType\":1,\"tag_id\":\"25\",\"ck_source\":\"\",\"thive_source\":\"\",\"label_valid\":0,\"calc_valid\":0,\"tag_express_option\":\"\",\"tag_express_value\":\"\"},{\"tag_name\":\"company\",\"tag_comment\":\"Email\",\"logicType\":1,\"inputValue\":\"3\",\"opType\":1,\"tag_id\":\"25\",\"ck_source\":\"\",\"thive_source\":\"\",\"label_valid\":0,\"calc_valid\":0,\"tag_express_option\":\"\",\"tag_express_value\":\"\"}],\"orderby\":{\"orderfield\":\"tittle\",\"orderType\":1},\"idNum\":1}",
                    "tag_list": [
                        {
                            "tag_id": "1",
                            "tag_name": "test1",
                            "tag_comment": "comment1",
                            "ck_source": "source1",
                            "thive_source": "souce2",
                            "label_valid":True,
                            "calc_valid":True,
                            "tag_express_option": "\u003c",
                            "tag_express_value": "1"
                        },
                        {
                            "tag_id": "2",
                            "tag_name": "test2",
                            "tag_comment": "comment2",
                            "ck_source": "source2",
                            "thive_source": "souce3",
                            "label_valid":True,
                            "calc_valid":True,
                            "tag_express_option": "\u003e",
                            "tag_express_value": "2"
                        }
                    ],
                    "extracted_count": "0",
                    "order_by": ""
                },
                {
                    "task_id": "12",
                    "task_name": "okkk",
                    "game": "hok",
                    "state": 1,
                    "create_time": "1697794781",
                    "update_time": "1698203636",
                    "data_version": "6",
                    "creator": "xiaoming",
                    "analysze_sql": "SELECT * FROM test",
                    "extract_sql": "SELECT * FROM test",
                    "output": "",
                    "analysis_result": "",
                    "tag_list": [
                        {
                            "tag_id": "1",
                            "tag_name": "test1",
                            "tag_comment": "comment1",
                            "ck_source": "source1",
                            "thive_source": "souce2",
                            "label_valid":True,
                            "calc_valid":True,
                            "tag_express_option": "\u003c",
                            "tag_express_value": "1"
                        },
                        {
                            "tag_id": "2",
                            "tag_name": "test2",
                            "tag_comment": "comment2",
                            "ck_source": "source2",
                            "thive_source": "souce3",
                            "label_valid":True,
                            "calc_valid":True,
                            "tag_express_option": "\u003e",
                            "tag_express_value": "2"
                        }
                    ],
                    "extracted_count": "0",
                    "order_by": ""
                }
            ],
            "total": "0"
        }
    )


@app.route('/api/v1/portal/get_extraction_task', methods=['GET'])
def user_deleted():
    taskId = flask.request.args.get('task_id')
    if taskId == 0:
        return flask.jsonify({
            {"ret_code": "-1","message": "task_id is nill","data":{}}
        })
    return flask.jsonify(
        {
            {"err_msg": "0","err_msg": "0"}
        }
    )


@app.route('/api/v1/portal/commit_task', methods=['POST'])
def push_task():
    task_name = flask.request.args.get('task_name')
    if task_name == '':
        return flask.jsonify(
            {"ret_code": "-1","message": "task_name is null","data":{}}
        )
    return flask.jsonify({
        {"err_msg": "0","err_msg": "0"}
    })


@app.route('/api/v1/portal/delete_task', methods=['POST'])
def taskDelete():
    return flask.jsonify(
        {"err_code": "0","err_msg": "0"}
    )
    
@app.route('/api/v1/portal/get_fieldlabel_list',methods=['POST'])
def labels():
    return flask.jsonify(
       {"err_code":"0","err_msg":"0","tag_list":[{"tag_id":"21","tag_name":"id","tag_comment":"ID","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"22","tag_name":"name","tag_comment":"用户名","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"23","tag_name":"age","tag_comment":"Age","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"24","tag_name":"gender","tag_comment":"Gender","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"25","tag_name":"email","tag_comment":"Email","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"26","tag_name":"phone","tag_comment":"Phone","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"27","tag_name":"address","tag_comment":"Address","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"28","tag_name":"salary","tag_comment":"Salary","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"29","tag_name":"company","tag_comment":"Company","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"30","tag_name":"title","tag_comment":"Title","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"31","tag_name":"experience","tag_comment":"Experience","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"32","tag_name":"education","tag_comment":"Education","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"33","tag_name":"language","tag_comment":"Language","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"34","tag_name":"interest","tag_comment":"Interest","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"35","tag_name":"height","tag_comment":"Height","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"36","tag_name":"weight","tag_comment":"Weight","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"37","tag_name":"blood_type","tag_comment":"Blood_type","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"38","tag_name":"register_date","tag_comment":"Register_date","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"39","tag_name":"update_time","tag_comment":"Update_time","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""},{"tag_id":"40","tag_name":"is_active","tag_comment":"Is_active","ck_source":"","thive_source":"","label_valid":0,"calc_valid":0,"tag_express_option":"","tag_express_value":""}]}
    )

@app.route('/api/v1/portal/get_production_list',methods=['GET'])
def production():
    return flask.jsonify(
        {
    "err_code": "0",
    "err_msg": "0",
    "game_list": [
        {
            "target": "10.190.24.126:9000/test",
            "table_name": "test",
            "game": "hok"
        }
    ]
}
    )

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
