import numpy as np
import cv2

class ImageProcessor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def additive_noise(image, percent):
        ### Вариант 1,5
        return np.clip(np.where(np.random.rand(*image.shape) < percent / 100,
                        image + np.random.randint(-20, 20, image.shape), image), 0, 255)

    @staticmethod
    def mean_filter(image, kernel_size):

        return cv2.blur(image, (kernel_size, kernel_size))
    
    @staticmethod
    def gauss_filter(image, kernel_size):
        sigma = kernel_size // 2 / 3

        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    
    @staticmethod
    def image_equalization(image):
        return cv2.equalizeHist(image)

    @staticmethod
    def statistic_correction(image, new_mean, new_std):
        image = image.astype(np.float32)
        mean, std = image.mean(), image.std()
        
        corrected_image = (image - mean) * (new_std / std) + new_mean
        corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)
        
        return corrected_image


    @staticmethod
    def resize(image, new_width, new_height):

        return cv2.resize(image, (new_width, new_height))

    @staticmethod
    def shift(image, x, y):
        return np.roll(np.roll(image, x, axis=1), y, axis=0)

    
    @staticmethod
    def rotation(image, k, l, angle):

        from scipy.ndimage import affine_transform
        angle_rad = np.deg2rad(angle)

        rotation_matrix = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad)],
            [np.sin(angle_rad), np.cos(angle_rad)]
        ])
        
        translation_to_origin = np.array([l, k])
        offset = translation_to_origin - rotation_matrix @ translation_to_origin
        
        rotated_image = affine_transform(image, rotation_matrix, offset=offset, order=1)
        
        return rotated_image.astype(int)

    @staticmethod
    def glass_effect(image):

        height, width = image.shape[:2]
        x, y = np.meshgrid(np.arange(width), np.arange(height))

        rand_x = np.clip(x + np.random.randint(-5, 6, x.shape), 0, width - 1)
        rand_y = np.clip(y + np.random.randint(-5, 6, y.shape), 0, height - 1)

        return image[rand_y, rand_x]
    
    @staticmethod
    def waves(image):
        height, width = image.shape[:2]
        x, y = np.meshgrid(np.arange(width), np.arange(height))
        rand_x = np.clip(x + 20 * np.sin(2 * np.pi * y / 30), 0, width - 1).astype(int)
        return image[y, rand_x]
    
    @staticmethod
    def motion_blur(image, n):
        T = np.zeros((n, n))
        np.fill_diagonal(T, 1 / n)
        return cv2.filter2D(image, -1, T)

