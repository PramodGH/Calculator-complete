                    {% for i in number_of_letters %}-->
                        <strong style="text-decoration: underline">Letter {{str_without_spaces[i]}}</strong>
                        <p>{{str_without_spaces[i]}} is letter number {{no_to_alpha_values[i]}} in the alphabet grid above</p>
                        <p>With x = {{no_to_alpha_values[i]}}, we have E({{no_to_alpha_values[i]}}) = {{a}}({{no_to_alpha_values[i]}}) + {{b}} = {{ mid_values[i] }} + {{b}} = {{final_values[i]}}</p>
                        <p>we have (ax+b) mod m = {{ final_values[i] }} mod 26 = {{ mod_values[i] }}</p>
                        <p>Finally, looking up the letter in our original grid, we have the cipher text for {{ mod_values[i] }} = {{ no_to_alpha_values[i] }}</p>
                        <br><br>

                    {% endfor %}



<!--                    {% for i,j,k,l,m,n in str_without_spaces,no_corres_to_alpha_values,no_to_alpha_values,mid_values,final_values,mod_values %}-->
<!--                        <strong style="text-decoration: underline">Letter {{i}}</strong>-->
<!--                        <p>{{i}} is letter number {{j}} in the alphabet grid above</p>-->
<!--                        <p>With x = {{j}}, we have E({{j}}) = {{a}}({{j}}) + {{b}} = {{ l }} + {{b}} = {{m}}</p>-->
<!--                        <p>we have (ax+b) mod m = {{ m }} mod 26 = {{ n }}</p>-->
<!--                        <p>Finally, looking up the letter in our original grid, we have the cipher text for {{ n }} = {{ k}}</p>-->
<!--                        <br><br>-->

<!--                    {% endfor %}-->
<!--                    itr_list-->



<!--                    {% for i in itr_list %}-->
<!--                        <strong style="text-decoration: underline">Letter {{str_without_spaces[i]}}</strong>-->
<!--                        <p>{{str_without_spaces[i]}} is letter number {{no_to_alpha_values[i]}} in the alphabet grid above</p>-->
<!--                        <p>With x = {{no_to_alpha_values[i]}}, we have E({{no_to_alpha_values[i]}}) = {{a}}({{no_to_alpha_values[i]}}) + {{b}} = {{ mid_values[i] }} + {{b}} = {{final_values[i]}}</p>-->
<!--                        <p>we have (ax+b) mod m = {{ final_values[i] }} mod 26 = {{ mod_values[i] }}</p>-->
<!--                        <p>Finally, looking up the letter in our original grid, we have the cipher text for {{ mod_values[i] }} = {{ no_to_alpha_values[i] }}</p>-->
<!--                        <br><br>-->

<!--                    {% endfor %}-->