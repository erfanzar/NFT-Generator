import os
import sys

import cv2 as cv
import numpy as np

images_format = [
    'jpg',
    'png',

]

input_format_name_founder = [list, tuple, int]
__back_ground_union = [list, str, tuple]


def reader(
        files: input_format_name_founder
):
    return [f for f in os.listdir(files) if os.path.exists(os.path.join(files, f)) and f.endswith('.png')]


def name_founder(
        files: input_format_name_founder
):
    __all = []
    __oranges = []
    __blue = []
    for i in files:
        i.lower()
        if i[0:5] == 'orange':
            __oranges.append(i)
        if i[0:3] == 'blue':
            __blue.append(i)

    return __all


class Dependencies:
    def __init__(self):
        super().__init__()
        self.in_use = True

    def founder(self, files: [list, tuple, int]):
        if self.in_use:
            return reader(files)

    def sort(self, files: [list, tuple, int]):
        if self.in_use:
            return name_founder(files)


class Generator(Dependencies):
    def __init__(
            self,
            path: str = None,
            back_ground: [list, str, tuple] = None,
            body: [list, str, tuple] = None,
            eyes: [list, str, tuple] = None,
            face: [list, str, tuple] = None,
            ears: [list, str, tuple] = None,
            glasses: [list, str, tuple] = None,
            neck_ls: [list, str, tuple] = None,
            piercing: [list, str, tuple] = None,
    ):

        super().__init__()

        # Check Vars

        self.neck_ls = neck_ls
        self.glasses = glasses
        self.ears = ears
        self.eyes = eyes
        self.face = face
        self.piercing = piercing
        self.body = body
        self.back_ground = back_ground
        self.path = path
        self.neck_ls_length = len(neck_ls) if neck_ls is not None else None
        self.glasses_length = len(glasses) if glasses is not None else None
        self.ears_length = len(ears) if ears is not None else None
        self.eyes_length = len(eyes) if eyes is not None else None
        self.face_length = len(face) if face is not None else None
        self.piercing_length = len(piercing) if piercing is not None else None
        self.body_length = len(body) if body is not None else None
        self.back_ground_length = len(back_ground) if back_ground is not None else None
        self.frame = None

        # Random Vars
        self.use_piercing = np.random.randint(0, 1)
        self.use_glasses = np.random.randint(0, 1)
        self.use_neck_ls = np.random.randint(0, 1)
        self.random_glass = np.random.randint(0, self.glasses_length) if self.glasses_length is not None else None
        self.random_neck_ls = np.random.randint(0, self.neck_ls_length) if self.neck_ls_length is not None else None
        self.random_piercing = np.random.randint(0, self.piercing_length) if self.piercing_length is not None else None

    def show(self):
        if self.frame is not None:
            while True:
                cv.imshow('nft_g', self.frame)
                cv.waitKey(1)
                if cv.waitKey(1) == ord('q'):
                    break
        else:
            sys.stdout.write('No BackGround Found')

    def forward(self):
        if self.back_ground is not None:

            # check the length of backgrounds
            for bg_i in range(self.back_ground_length):

                self.frame = cv.imread(f'{self.path}/{self.back_ground[bg_i]}', cv.IMREAD_UNCHANGED)
                print(self.frame.shape)

                # check if is anybody is available

                if self.body is not None:
                    for body_i in range(self.body_length):
                        body = cv.imread(f'{self.path}/{self.body[body_i]}', cv.IMREAD_UNCHANGED)
                        self.frame[0:body.shape[0], 0:body.shape[1], 0:3] = body

                        # check if any face is available

                        if self.face is not None:
                            for face_i in range(self.face_length):
                                face = cv.imread(f'{self.path}/{self.face[face_i]}', cv.IMREAD_UNCHANGED)
                                self.frame[0:face.face[0], 0:face.face[1]] = face

                                if self.eyes is not None:
                                    for eyes_i in range(self.eyes_length):
                                        eyes = cv.imread(f'{self.path}/{self.eyes[eyes_i]}', cv.IMREAD_UNCHANGED)
                                        self.frame[0:eyes.shape[0], 0:eyes.shape[1]] = eyes

                                        if self.piercing is not None and self.use_piercing == 1:
                                            piercing = cv.imread(f'{self.path}/{self.piercing[self.piercing_length]}',
                                                                 cv.IMREAD_UNCHANGED)
                                            self.frame[0:piercing.shape[0], 0:piercing.shape[1]] = piercing
                                            self.use_piercing = np.random.randint(0, 1)

                                            self.random_piercing = np.random.randint(0, self.piercing_length)
                                        else:
                                            self.use_piercing = np.random.randint(0, 1)
                                        if self.neck_ls is not None and self.use_neck_ls == 1:
                                            neck_ls = cv.imread(f'{self.path}/{self.neck_ls[self.neck_ls_length]}',
                                                                cv.IMREAD_UNCHANGED)
                                            self.frame[0:neck_ls.shape[0], 0:neck_ls.shape[1]] = neck_ls
                                            self.use_neck_ls = np.random.randint(0, 1)

                                            self.random_neck_ls = np.random.randint(0, self.neck_ls_length)
                                        else:
                                            self.use_neck_ls = np.random.randint(0, 1)
                                        if self.glasses is not None and self.use_glasses == 1:
                                            glasses = cv.imread(f'{self.path}/{self.glasses[self.glasses_length]}',
                                                                cv.IMREAD_UNCHANGED)
                                            self.frame[0:glasses.shape[0], 0:glasses.shape[1]] = glasses
                                            self.use_glasses = np.random.randint(0, 1)
                                            self.random_glass = np.random.randint(0, self.glasses_length)
                                        else:
                                            self.use_glasses = np.random.randint(0, 1)


list_bg = reader('E:/Python/NFT-Generator/images')

gen_nft = Generator(path='images', back_ground=list_bg)
gen_nft.forward()
vva = gen_nft.founder('E:/Python/NFT-Generator/images')
print(vva)
gen_nft.show()
