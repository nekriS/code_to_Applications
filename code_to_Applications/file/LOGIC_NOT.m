

function output_image = LOGIC_NOT(image_1_)
    [x1, y1, z] = size(image_1_);

    if IMG_CNORM(image_1_) == 1
        MAX = 1; %БИНАРНОЕ ИЗОБРАЖЕНИЕ
    else
        MAX = 255; 
    end

    output_image_ = zeros(x1, y1, z);
    
        
    for i = 1:x1
        for j = 1:y1
            for g = 1:z
                output_image_(i, j, g) = MAX - image_1_(i, j, g);
            end
        end
    end
    
    
    output_image = im2uint8(output_image_ ./ MAX);

end

