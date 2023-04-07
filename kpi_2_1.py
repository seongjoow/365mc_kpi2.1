import pandas as pd
import glob

class Kpi:
    def __init__(self):
        # customerID(str): 고객번호입니다.
        # date(str): 수술일자입니다.
        # cam(str): Cam번호입니다. '1' 또는 '2'의 값을 갖습니다. Cam을 기준으로 프레임 정보를 갱신합니다.
        # section_size(int): 전체 수술을 등시간으로 나눌 때 구간의 길이입니다. 단위는 프레임입니다.
        # acceptable_missing_frames(int): 스트로크를 정의할 때, 두 극소점 사이 허용되는 연속 결측 프레임 개수입니다.
        # max_cluster_number(int): 각 수술의 클러스터의 수는 상이하기 때문에, 최종 결과의 형식을 통일하기 위한 최대 클러스터 개수입니다.
        # max_section_number(int): 각 수술의 길이는 상이하기 때문에, 최종 결과의 형식을 통일하기 위한 최대 구간 개수입니다.

        # cluster_count(int): 해당 수술의 클러스터 개수입니다.
        # max_frame_number(int): 해당 Cam의 수술의 전체 영상의 마지막 프레임 번호입니다. 
        # frame_count(int): 해당 Cam의 수술 전체 영상의 총 프레임 개수입니다. 
        # missing_frame_count(int): 해당 Cam의 결측 프레임 개수입니다.
        # cluster_path_list(list): 해당 수술의 클러스터 파일 경로 리스트입니다.
        # whole_surgery_data_path(str): 해당 전체 수술에 대한 파일 경로입니다.

        # Options
        self.customerID: str = None
        self.date: str = None
        self.cam: str = None
        self.section_size: int = None
        self.acceptable_missing_frames: int = None
        self.max_cluster_number: int = None
        self.max_section_number: int = None

        # Info of Data
        self.cluster_count: int = None
        self.max_frame_number: int = None
        self.frame_count: int = None
        self.missing_frame_count: int = None
        self.cluster_path_list: list = None
        self.whole_surgery_data_path: str = None

        # Status
        self.put_options_done: bool = False
        self.put_data_path_done: bool = False


    def summary(self):
        # 수술 정보를 출력합니다.
        # 1. 고객번호
        # 2. 수술일자
        # 3. Cam번호
        # 4. 클러스터 개수
        # 5. 최대 프레임 번호
        # 6. 총 프레임 개수
        # 7. 결측 프레임 개수

        pass


    def manager(self, message: str):
        if message == "put_options_done":
            self.put_options_done = True

        if message == "put_data_path_done":
            self.put_data_path_done = True


    def put_options(self, 
                    customerID: str, 
                    date: str, 
                    cam: str, 
                    acceptable_missing_frames: int, 
                    section_size: int, 
                    max_cluster_number: int,
                    max_section_number: int):

        self.manager(message='put_options_done')


    def put_data_path(self, folder: str):
        # 수술 정보의 최상위 폴더 경로를 입력 받습니다.

        self.manager(message='put_data_path_done')


    def cal_lowest_point(self, data_path: str) -> list:
        result = list()

        df = pd.read_csv(data_path)

        # 입력받은 데이터에서 집도의의 손의 속도의 극소점을 찾습니다.
        # 극소점의 프레임 번호를 리스트로 return
        # return되는 리스트의 len()값이 극소점의 개수입니다.
        # return ex. [30, 54, 72, ...]

        return result


    def count_valid_stroke(self, lowest_points_list: list, data_path: str) -> int:
        unidentified_strokes = len(lowest_points_list) - 1
        unvalid_stokes = 0

        df = pd.read_csv(data_path)

        # 극소점의 프레임 번호 리스트를 이용하여 유효한 스트로크 개수를 return
        # 두 극소점 사이에 존재하는 연속 결측 프레임 개수가 self.acceptable_missing_frames 미만이면
        # 해당 두 극소점을 잇는 스트로크는 유효한 스트로크로 정의합니다.
        # 모든 스트로크가 유효할 경우, 스트로크 개수는 (극소점 개수 - 1)입니다.
        # cal_lowest_point() 사용 권장
        # return ex. 1029

        return unidentified_strokes - unvalid_stokes


    def cal_all_cluster_stroke(self) -> list:
        assert self.put_options_done == True, "옵션이 설정되지 않았습니다. put_options()를 이용해 옵션을 설정해주세요."
        assert self.put_data_path_done == True, "Data path가 설정되지 않았습니다. put_data_path()를 이용해 파일의 경로를 설정해주세요."

        result = list()

        # 모든 클러스터에 대하여 각 클러스터의 스트로크 개수를 구하고
        # 이를 리스트로 return
        # return ex. [123, 23, 1029, 0, 23, ...]
        # count_valid_stroke() 사용 권장
        # 주의: 클러스터 번호는 1번부터 시작, Cam 정보를 사용할 것

        return result


    def cal_whole_surgery_stroke(self) -> list:
        assert self.put_options_done == True, "옵션이 설정되지 않았습니다. put_options()를 이용해 옵션을 설정해주세요."
        assert self.put_data_path_done == True, "Data path가 설정되지 않았습니다. put_data_path()를 이용해 파일의 경로를 설정해주세요."

        result = list()

        # 전체 수술 데이터에 대하여 구간별 스트로크 개수를 구하고
        # 이를 리스트로 return
        # return ex. [324, 23, 2218, 0, 21, ...]
        # 주의: Cam 정보를 사용할 것

        return result


    def return_result_dict(self) -> dict():
        # 클러스터와 구간별 스트로크 개수를 계산합니다.
        all_cluster_stroke = self.cal_all_cluster_stroke(self)
        whole_surgery_stroke = self.cal_whole_surgery_stroke(self)

        # 결과를 dict로 return합니다.
        result = dict()

        # 결과 dict의 형식을 통일하기 위해 스트로크 개수와 구간의 개수 만큼 key를 만듭니다.
        # 정보가 없는 클러스터와 구간에는 스트로크 개수를 0으로 설정합니다.
        for i in range(1, self.max_cluster_number+1):
            result['NumberOfStrokes_cluster'+str(i)] = 0

        for i in range(1, self.max_section_number+1):
            result['NumberOfStrokes_section'+str(i)] = 0

        # 결과 dict에 고객번호, 수술일자 정보와 계산된 스트로크 정보를 입력합니다.
        result['customerID'] = self.customerID
        result['date'] = self.date
        for i in range(1, len(all_cluster_stroke)+1):
            result['NumberOfStrokes_cluster'+str(i)] = all_cluster_stroke[i-1]
        for i in range(1, len(whole_surgery_stroke)+1):
            result['NumberOfStrokes_section'+str(i)] = whole_surgery_stroke[i-1]

        # 결과를 return
        return result
    

    # Result Example
    # {
    #     "customerID" : asd,
    #     "date": asd,
    #     "NumberOfStrokes_cluster1": 10,
    #     "NumberOfStrokes_cluster2": 100,
    #     ...
    #     "NumberOfStrokes_section1": 30,
    #     "NumberOfStrokes_section2": 130,
    #     ...
    # }