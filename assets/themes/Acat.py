from __future__ import annotations

from typing import Iterable
import gradio as gr

#gr.themes.builder()
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
import time

class Acat(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.green,
        secondary_hue: colors.Color | str = colors.emerald,
        neutral_hue: colors.Color | str = colors.neutral,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            'Inter V',
            fonts.GoogleFont('Asap'),
            'ui-sans-serif',
            'sans-serif',
        ),
        font_mono: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            'ui-monospace',
            fonts.GoogleFont("Fira Code"),
            'Consolas',
            'monospace',
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        self.name= "Acat",
        self.secondary_100='#e2effc',
        self.secondary_200='#bedff9',
        self.secondary_300='#84c5f5',
        self.secondary_400='#4eacef',
        self.secondary_50='#f1f8fe',
        self.secondary_500='#198cde',
        self.secondary_600='#0c6ebd',
        self.secondary_700='#0b5899',
        self.secondary_800='#0e4b7e',
        self.secondary_900='#113f69',
        self.secondary_950='#0b2846',
        self.neutral_100='#e2effc',
        self.neutral_200='#bedff9',
        self.neutral_300='#84c5f5',
        self.neutral_400='#4eacef',
        self.neutral_50='#f1f8fe',
        self.neutral_500='#198cde',
        self.neutral_600='#0c6ebd',
        self.neutral_700='#0b5899',
        self.neutral_800='#0e4b7e',
        self.neutral_900='#113f69',
        self.neutral_950='#0b2846',
        self.primary_100='#e2effc',
        self.primary_200='#bedff9',
        self.primary_300='#84c5f5',
        self.primary_400='#4eacef',
        self.primary_50='#f1f8fe',
        self.primary_500='#198cde',
        self.primary_600='#0c6ebd',
        self.primary_700='#0b5899',
        self.primary_800='#0e4b7e',
        self.primary_900='#113f69',
        self.primary_950='#0b2846',
        super().set(
            # Blaise
            background_fill_primary='#FFFFFF',
            background_fill_primary_dark='#000000',
            background_fill_secondary='#dce3e8',
            background_fill_secondary_dark='#242424',
            block_background_fill='#ECF2F7',
            block_background_fill_dark='#191919',
            block_border_color='#dce3e8',
            block_border_color_dark='#242424',
            block_border_width='1px',
            block_info_text_color='#191919',
            block_info_text_color_dark='#ECF2F7',
            block_info_text_size='*text_sm',
            block_info_text_weight='400',
            block_label_background_fill='#ECF2F700',
            block_label_background_fill_dark='#19191900',
            block_label_border_color='#dce3e8',
            block_label_border_color_dark='#242424',
            block_label_border_width='1px',
            block_label_margin='0',
            block_label_padding='*spacing_sm *spacing_lg',
            block_label_radius= "calc(*radius_lg - 1px) 0 calc(*radius_lg - 1px) 0",
            block_label_right_radius= "0 calc(*radius_lg - 1px) 0 calc(*radius_lg - 1px)",
            block_label_shadow='*block_shadow',
            block_label_text_color='#4EACEF',
            block_label_text_color_dark='#4EACEF',
            block_label_text_size='*text_sm',
            block_label_text_weight='400',
            block_padding='*spacing_xl calc(*spacing_xl + 2px)',
            block_radius='*radius_lg',
            block_shadow='#FFFFFF00',
            block_shadow_dark='#00000000',
            block_title_background_fill='#ECF2F700',
            block_title_background_fill_dark='#19191900',
            block_title_border_color='#dce3e8',
            block_title_border_color_dark='#242424',
            block_title_border_width='0px',
            block_title_padding='0',
            block_title_radius='none',
            block_title_text_color='#4EACEF',
            block_title_text_color_dark='#4EACEF',
            block_title_text_size='*text_md',
            block_title_text_weight='bold',
            body_background_fill="url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/374e309d-713c-4ef2-b941-912bd95a5d52/deblqm8-4885280f-af38-41ef-9a32-9e6cc463de9c.png/v1/fill/w_1920,h_1600/__xiao__render__by_stardustinqs_deblqm8-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTYwMCIsInBhdGgiOiJcL2ZcLzM3NGUzMDlkLTcxM2MtNGVmMi1iOTQxLTkxMmJkOTVhNWQ1MlwvZGVibHFtOC00ODg1MjgwZi1hZjM4LTQxZWYtOWEzMi05ZTZjYzQ2M2RlOWMucG5nIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.d1-eWOY8oZTGcy12ZsV3_4Z1wGRXZeEmVnJYx-EF5zI') #FFFFFF no-repeat right bottom/auto 30svh padding-box fixed",
            body_background_fill_dark="url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/374e309d-713c-4ef2-b941-912bd95a5d52/deblqm8-4885280f-af38-41ef-9a32-9e6cc463de9c.png/v1/fill/w_1920,h_1600/__xiao__render__by_stardustinqs_deblqm8-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTYwMCIsInBhdGgiOiJcL2ZcLzM3NGUzMDlkLTcxM2MtNGVmMi1iOTQxLTkxMmJkOTVhNWQ1MlwvZGVibHFtOC00ODg1MjgwZi1hZjM4LTQxZWYtOWEzMi05ZTZjYzQ2M2RlOWMucG5nIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.d1-eWOY8oZTGcy12ZsV3_4Z1wGRXZeEmVnJYx-EF5zI') #000000 no-repeat right bottom/auto 30svh padding-box fixed",
            body_text_color='#191919',
            body_text_color_dark='#ECF2F7',
            body_text_color_subdued='#636668',
            body_text_color_subdued_dark='#c4c4c4',
            body_text_size='*text_md',
            body_text_weight='400',
            border_color_accent='#dce3e8',
            border_color_accent_dark='#242424',
            border_color_primary='#dce3e8',
            border_color_primary_dark='#242424',
            button_border_width='*input_border_width',
            button_border_width_dark='*input_border_width',
            button_cancel_background_fill='#dce3e8',
            button_cancel_background_fill_dark='#242424',
            button_cancel_background_fill_hover='#d0d7db',
            button_cancel_background_fill_hover_dark='#202020',
            button_cancel_border_color='#191919',
            button_cancel_border_color_dark='#ECF2F7',
            button_cancel_border_color_hover='#202020',
            button_cancel_border_color_hover_dark='#a1c3d8',
            button_cancel_text_color='#4EACEF',
            button_cancel_text_color_dark='#4EACEF',
            button_cancel_text_color_hover='#0c6ebd',
            button_cancel_text_color_hover_dark='#0c6ebd',
            button_large_padding='*spacing_lg calc(2 * *spacing_lg)',
            button_large_radius='*radius_lg',
            button_large_text_size='*text_lg',
            button_large_text_weight='600',
            button_primary_background_fill='#4EACEF',
            button_primary_background_fill_dark='#4EACEF',
            button_primary_background_fill_hover='#0c6ebd',
            button_primary_background_fill_hover_dark='#0c6ebd',
            button_primary_border_color='#191919',
            button_primary_border_color_dark='#ECF2F7',
            button_primary_border_color_hover='#202020',
            button_primary_border_color_hover_dark='#a1c3d8',
            button_primary_text_color='#ECF2F7',
            button_primary_text_color_dark='#191919',
            button_primary_text_color_hover='#e1eaf0',
            button_primary_text_color_hover_dark='#141414',
            button_secondary_background_fill='#dce3e8',
            button_secondary_background_fill_dark='#242424',
            button_secondary_background_fill_hover='#d0d7db',
            button_secondary_background_fill_hover_dark='#202020',
            button_secondary_border_color='#dce3e8',
            button_secondary_border_color_dark='#242424',
            button_secondary_border_color_hover='#d0d7db',
            button_secondary_border_color_hover_dark='#202020',
            button_secondary_text_color='#4EACEF',
            button_secondary_text_color_dark='#4EACEF',
            button_secondary_text_color_hover='#0c6ebd',
            button_secondary_text_color_hover_dark='#0c6ebd',
            button_shadow='none',
            button_shadow_active='none',
            button_shadow_hover='none',
            button_small_padding='*spacing_sm calc(2 * *spacing_sm)',
            button_small_radius='*radius_lg',
            button_small_text_size='*text_md',
            button_small_text_weight='400',
            button_transition='background-color 0.2s ease',
            chatbot_code_background_color='#FFFFFF',
            chatbot_code_background_color_dark='#000000',
            checkbox_background_color='#dce3e8',
            checkbox_background_color_dark='#242424',
            checkbox_background_color_focus='#dce3e8',
            checkbox_background_color_focus_dark='#242424',
            checkbox_background_color_hover='#dce3e8',
            checkbox_background_color_hover_dark='#242424',
            checkbox_background_color_selected='#4EACEF',
            checkbox_background_color_selected_dark='#4EACEF',
            checkbox_border_color='#dce3e8',
            checkbox_border_color_dark='#242424',
            checkbox_border_color_focus='#4EACEF',
            checkbox_border_color_focus_dark='#4EACEF',
            checkbox_border_color_hover='#4EACEF',
            checkbox_border_color_hover_dark='#4EACEF',
            checkbox_border_color_selected='#4EACEF',
            checkbox_border_color_selected_dark='#4EACEF',
            checkbox_border_radius='*radius_sm',
            checkbox_border_width='1px',
            checkbox_border_width_dark='1px',
            checkbox_check= "url(\"data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e\")",
            checkbox_label_background_fill='#ECF2F7',
            checkbox_label_background_fill_dark='#191919',
            checkbox_label_background_fill_hover='#dce3e8',
            checkbox_label_background_fill_hover_dark='#242424',
            checkbox_label_background_fill_selected='#dce3e8',
            checkbox_label_background_fill_selected_dark='#242424',
            checkbox_label_border_color='#dce3e8',
            checkbox_label_border_color_dark='#242424',
            checkbox_label_border_color_hover='#4EACEF',
            checkbox_label_border_color_hover_dark='#4EACEF',
            checkbox_label_border_width='1px',
            checkbox_label_border_width_dark='1px',
            checkbox_label_gap='*spacing_lg',
            checkbox_label_padding='*spacing_md calc(2 * *spacing_md)',
            checkbox_label_shadow='none',
            checkbox_label_text_color='#191919',
            checkbox_label_text_color_dark='#ECF2F7',
            checkbox_label_text_color_selected='#4EACEF',
            checkbox_label_text_color_selected_dark='#4EACEF',
            checkbox_label_text_size='*text_md',
            checkbox_label_text_weight='400',
            checkbox_shadow='*input_shadow',
            color_accent='*primary_500',
            color_accent_soft='#dce3e8',
            color_accent_soft_dark='#242424',
            container_radius='*radius_lg',
            embed_radius='*radius_lg',
            error_background_fill='#dce3e8',
            error_background_fill_dark='#242424',
            error_border_color='#191919',
            error_border_color_dark='#ECF2F7',
            error_border_width='1px',
            error_border_width_dark='1px',
            error_text_color='#4EACEF',
            error_text_color_dark='#4EACEF',
            form_gap_width='0px',
            input_background_fill='#dce3e8',
            input_background_fill_dark='#242424',
            input_background_fill_focus='#dce3e8',
            input_background_fill_focus_dark='#242424',
            input_background_fill_hover='#d0d7db',
            input_background_fill_hover_dark='#202020',
            input_border_color='#191919',
            input_border_color_dark='#ECF2F7',
            input_border_color_focus='#191919',
            input_border_color_focus_dark='#ECF2F7',
            input_border_color_hover='#202020',
            input_border_color_hover_dark='#a1c3d8',
            input_border_width='0px',
            input_padding='*spacing_xl',
            input_placeholder_color='#19191930',
            input_placeholder_color_dark='#ECF2F730',
            input_radius='*radius_lg',
            input_shadow='#19191900',
            input_shadow_dark='#ECF2F700',
            input_shadow_focus='#19191900',
            input_shadow_focus_dark='#ECF2F700',
            input_text_size='*text_md',
            input_text_weight='400',
            layout_gap='*spacing_xxl',
            link_text_color='#4EACEF',
            link_text_color_active='#4EACEF',
            link_text_color_active_dark='#4EACEF',
            link_text_color_dark='#4EACEF',
            link_text_color_hover='#0c6ebd',
            link_text_color_hover_dark='#0c6ebd',
            link_text_color_visited='#4EACEF',
            link_text_color_visited_dark='#4EACEF',
            loader_color='#4EACEF',
            loader_color_dark='#4EACEF',

            panel_background_fill='#ECF2F7',
            panel_background_fill_dark='#191919',
            panel_border_color='#4EACEF',
            panel_border_color_dark='#4EACEF',
            panel_border_width='0',

            prose_header_text_weight='600',
            prose_text_size='*text_md',
            prose_text_weight='400',
            radio_circle= "url(\"data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='8' cy='8' r='3'/%3e%3c/svg%3e\")",
            section_header_text_size='*text_md',
            section_header_text_weight='400',
            shadow_drop='rgba(0,0,0,0.05) 0px 1px 2px 0px',
            shadow_drop_lg='0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
            shadow_inset='rgba(0,0,0,0.05) 0px 2px 4px 0px inset',
            shadow_spread='#FFFFFF',
            shadow_spread_dark='#000000',
            slider_color='#4EACEF',
            slider_color_dark='#4EACEF',
            stat_background_fill='#4EACEF',
            stat_background_fill_dark='#4EACEF',
            table_border_color='#191919',
            table_border_color_dark='#ECF2F7',
            table_even_background_fill='#ECF2F7',
            table_even_background_fill_dark='#191919',
            table_odd_background_fill='#dce3e8',
            table_odd_background_fill_dark='#242424',
            table_radius='*radius_lg',
            table_row_focus='#191919',
            table_row_focus_dark='#ECF2F7',

        )

